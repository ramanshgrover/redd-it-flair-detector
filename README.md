# Reddit Flair Detector
 A web application to detect flairs of [r/India](https://reddit.com/r/India/) posts. The application is live [here](https://redd-it-flair-detector.herokuapp.com/)
 
 ![](Demo.gif)

## Prerequisites, Dependencies and Execution
Ensure that you have  [Python3](https://www.python.org/downloads/)  and  [pip](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py)  installed on your specific distribution.

Open the Terminal and Clone the repository.
```
git clone https://github.com/ramanshgrover/redd-it-flair-detector/
```
Create a virtual environment.
``` 
python -m venv .env
source .env/bin/activate
```
**Downloading the spaCy and nltk dependencies:**
Execute the following command on your terminal.
```
python -m spacy download en_core_web_sm
```
Enter the Python console using `python3` , input the following and exit the shell
```
>>> import nltk
>>> nltk.download(‘stopwords’)
```
Now make sure you’re in the same directory as [_requirements.txt_](https://github.com/ramanshgrover/redd-it-flair-detector/blob/master/requirements.txt), and run the following command on your terminal.
```
pip3 install -r requirements.txt
``` 
***Disclaimer:*** _This may take a while._

Now, execute the following command: `python main.py`. It will direct to the _localhost_ with the _port_. Copy the IP Address to a web browser and use the flask app.

## Summary of the Methodology
To conclude, I sampled [r/India](https://reddit.com/r/India/) flairwise, (200 per flair, within PRAW constraints). The aforementioned dataset consisted of Hindi, English and code-mixed (Hinglish) text data. In this task, I clustered out the Hindi and the English portions of the data point scraped (URL+Title+Post+Comments). One of the main properties of such texts is that the English and the Hindi parts generally exist in groups. Hence, I tried to isolate them. 

I used the corpus generated from a dictionary, computed every word's [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) with words in our corpus starting from 'r' and having a length in range (l-2, l+2) where l is the length of the word in consideration. But for most code-mixed tokens scraped, depending upon the context, there will be a large levenshtein distance with respect to the corpus. Hence we alot a distance to every word and then finally apply the k-means algorithm to get two clusters of Code-Mixed Hinglish and English. Using the googletrans library, I translated the Code-Mixed Hindi written in Latin script to Devanagari.

Upon further EDA, I made sure to preprocess every class of flair to be independent of the others (in terms of the text distribution itself) and found out that TFIDF word vectors performed best with SVC (C=10, gamma=1, and the rbf kernel) achieving ~80.51% testing accuracy with a surprisingly large overfit. For detailed analysis, intuitions, observations and working do check out my [Jupyter Notebooks](https://github.com/ramanshgrover/redd-it-flair-detector/tree/master/notebooks).

|   Vectorizer  |    Multinomial Naive Bayes     |    Logistic Regression   | Random Forest | **Support Vector Machine** |
| :-----------: | :----------------------------: | :----------------------: | :-----------: | :------------------------: |
| Bag-of-Words  |               48.84            |            72.82         |     78.84     |            77.69           |
|  **TF IDF**   |               57.17            |            61.66         |     79.74     |          **80.51**         |
