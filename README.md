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
Now make sure you’re in the same directory as /requirements.txt/, and run the following command on your terminal.
```
python -m spacy download en 
pip3 install -r requirements.txt
``` 
*Disclaimer:* _This may take a while._

Now, execute the following command: `python main.py`. It will direct to the /localhost/ with the /port/. Copy the IP Address to a web browser and use the flask app.

## Summary
To conclude, I sampled r/India flair wise, (to the extent PRAW permitted) and found out that SVM with C=10, gamma=1, and the rbf kernel was able to achieve ~80.51% testing accuracy with a surprisingly large overfit.

