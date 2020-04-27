# Reddit Flair Detector
 A web application to detect flairs of [r/India](https://reddit.com/r/India/) posts. The application is live [here](https://redd-it-flair-detector.herokuapp.com/)
 
 ![](Demo.gif)

## Prerequisites, Dependencies and Execution
Ensure that you have  [Python3](https://www.python.org/downloads/)  and  [pip](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py)  installed on your specific distribution.

Open the Terminal and Clone the repository.
```
git clone https://github.com/ramanshgrover/
```
Create a virtual environment.
```
python -m venv .env
source .env/bin/activate
```
*Install the required Python libraries and frameworks.*
Run the Python console using `python3` , input the following and exit the shell
```
>>> import nltk
>>> nltk.download(‘stopwords’)
>>> nltk.download(‘wordnet’)
```
Now make sure you’re in the same directory as _requirements.txt_, and run the following command on your terminal.
```
python -m spacy download en 
pip3 install -r requirements.txt
``` 
*Disclaimer:* _This may take a while._

Now, execute the following command: `python main.py`. It will direct to the _localhost_ with the _port_. Copy the IP Address to a web browser and use the flask app.

## Summary
To conclude, I sampled [r/India](https://reddit.com/r/India/) flair wise, (200 per flair, within PRAW constraints) and found out that TFIDF word vectors performed best with SVC (C=10, gamma=1, and the rbf kernel) achieving ~80.51% testing accuracy with a surprisingly large overfit. For detailed analysis, intuitions, observations and working do check out my Jupyter Notebooks.

|   Vectorizer  |    Multinomial Naive Bayes     |    Logistic Regression   | Random Forest | **Support Vector Machine** |
| ------------- | ------------------------------ | ------------------------ | ------------- | -------------------------- |
| Bag-of-Words  |               48.84            |            72.82         |     78.84     |            77.69           |
|  **TF IDF**   |               57.17            |            61.66         |     79.74     |          **80.51**         |
