from flask import Flask, request, render_template, jsonify, json
import pandas as pd
import joblib
import pickle
import praw
import unicodedata
import re
import string
import spacy
import nltk
import sys
from nltk.corpus import stopwords
from sklearn.svm import SVC
import logging

app = Flask(__name__)

# logging to Heroku to debug runtime errors
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def home():
    return render_template('index.html')


# instance and authentication of the Web App bot
bot = praw.Reddit(client_id='td74lTDXbZJWoQ',
                  client_secret='UD_Lp2-7JhCKMdxfOI5pUvSqTqU',
                  redirect_uri='http://34.73.225.220:4444',
                  user_agent='AantiNashonalBot')

bot.read_only = True  # A submission read-only bot
subreddit = bot.subreddit('india')

# Flairs
flairs = ['Politics', 'Photography', 'Policy/Economy', 'AskIndia', 'Sports', 'Non-Political',
          'Scheduled', 'Science/Technology', 'Food', 'Business/Finance', 'Coronavirus', 'AMA', '[R]eddiquette']

# cleaning combined data
stop_words = stopwords.words('english')  # stopwords
extended = ['nan', 'https', 'http', 'redd', 'com', 'reddit', 'wwwredditcom', 'get',     'imgurcom', 'iimgurcom', 'www', 'x200b', 'nbsp', 'like', 'dont',
            'people', 'india', 'indian', 'time', 'good', 'want', 'think', 'know', 'need', 'make', 'thing', 'year', 'day', 'reddit', 'comments', 'comment']
stop_words.extend(extended)

# lemmatizing combined cleaned data
nlp = spacy.load('en_core_web_sm')
allowed_postags = ['PROPN', 'VERB', 'NOUN', 'ADV', 'ADJ']


def lemmatize_text(submission_df):
    try:
        lemmatized_submissions = []
        for submission in submission_df['combined_cleaned']:
            doc = nlp(submission)
            submission = [
                token.lemma_ for token in doc if token.pos_ in allowed_postags]
            lemmatized_submissions.append(" ".join(submission))
        submission_df['combined_lemmatized'] = lemmatized_submissions
        return submission_df
    except:
        submission_df['combined_lemmatized'] = submission_df['combined_cleaned']
        return submission_df


def unicodeToAscii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def clean_text(sentence):
    if type(sentence) == type('a'):
        sentence = unicodeToAscii(sentence.lower().strip())
        sentence = re.sub(r"([.!?])", r" \1", sentence)
        sentence = re.sub(r'[/(){}\[\]\|@,;:.]', r' ', str(sentence))
        sentence = re.sub(r"[^a-z]+", r" ", sentence)
        sentence = ' '.join(word for word in sentence.split()
                            if word not in stop_words and len(word) > 2)
        return sentence


def fetch_submission(url):
    submission = bot.submission(url=url)

    submission.comments.replace_more(limit=None)
    comments = ''
    for top_level_comment in submission.comments:
        comments += top_level_comment.body

    sub_dict = {
        "body": [submission.selftext],
        "comment": [comments],
        "created": [submission.created_utc],
        "id": [submission.id],
        "title": [submission.title],
        "url": [submission.url]
    }

    submission_df = pd.DataFrame.from_dict(sub_dict)
    submission_df['combined'] = submission_df['url'].map(str) + submission_df['title'].map(
        str) + submission_df['body'].map(str) + submission_df['comment'].map(str)
    submission_df['combined_cleaned'] = submission_df["combined"].apply(
        lambda x: clean_text(x))
    submission_df = lemmatize_text(submission_df)

    return submission_df


@app.route('/predict', methods=['POST'])
def predict():
    # loading tfidf vectorizer features
    vec = joblib.load('model/tfidf_vec.pkl')
    # loading the SVC
    model = joblib.load('model/SVM.pkl')

    if request.method == 'POST':
       # getting url as input from the form
        url = request.form['comment']

        # fetching, cleaning and lemmatizing the respective submission on that url
        submission_df = fetch_submission(str(url))

        # converting to tfidf vectors and predicting using the SVM Model
        X_test = vec.transform(submission_df["combined_lemmatized"])
        X_test_text_df = pd.DataFrame(X_test.todense(), columns=[
                                      x+'_text' for x in vec.get_feature_names()])
        predictions = model.predict(X_test_text_df)  # predictions

    return render_template('result.html', prediction=str(predictions[0]))


def predict_oup(link):
     # loading tfidf vectorizer features
    vec = joblib.load('model/tfidf_vec.pkl')
    # loading the SVC
    model = joblib.load('model/SVM.pkl')
    # fetching, cleaning and lemmatizing the respective submission on that url
    submission_df = fetch_submission(str(link))

    # converting to tfidf vectors and predicting using the SVM Model
    X_test = vec.transform(submission_df["combined_lemmatized"])
    X_test_text_df = pd.DataFrame(X_test.todense(), columns=[
                                  x+'_text' for x in vec.get_feature_names()])
    prediction = model.predict(X_test_text_df)  # predictions
    return str(prediction[0])


@app.route("/automated_testing", methods=['POST'])
def test():
    if request.files:
        file = request.files["upload_file"]
        sentences = file.read()
        urls = str(sentences.decode('utf-8')).split('\n')
        prediction = {}
        for url in urls:
            prediction[url] = predict_oup(url)
        return jsonify(prediction)
    else:
        return "Some Error Occurred!"


if __name__ == '__main__':
    app.run()
