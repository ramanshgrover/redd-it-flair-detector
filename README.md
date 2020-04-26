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
To conclude, I sampled r/India flair wise, (to the extent PRAW permitted) and found out that SVM with C=10, gamma=1, and the rbf kernel was able to achieve ~80.51% testing accuracy with a surprisingly large overfit.

|   Vectorizer  |     Model     |    Accuracy   |
| ------------- | ------------- | ------------- |
| Bag-of-Words  | Multinomial Naive Bayes 1  | 48.84  |
| Bag-of-Words  | Multinomial Naive Bayes 2  | 48.46 |
| Bag-of-Words  | Logistic Regression 1  |  70.64 |
| Bag-of-Words  | Logistic Regression 2  | 72.82 |
| Bag-of-Words  | Random Forest 1  | 77.94  |
| Bag-of-Words  | Random Forest 2  | 78.84 |
| Bag-of-Words  | Support Vector Machine 1  | 77.69 |
| Bag-of-Words  | Support Vector Machine 2 | 77.30 |
| TF IDF  | Multinomial Naive Bayes 1  | 56.28  |
| TF IDF  | Multinomial Naive Bayes 2  | 57.17 |
| TF IDF  | Logistic Regression 1  | 61.41  |
| TF IDF  | Logistic Regression 2  | 61.66 |
| TF IDF  | Random Forest 1  |   79.74 |
| TF IDF  | Random Forest 2  |  78.71 |
| TF IDF  | Support Vector Machine 1  |  66.92  |
| TF IDF  | Support Vector Machine 2 | **80.51** |
