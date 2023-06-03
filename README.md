# Spam-email-detector
This is machine learning model and vectorizer. And the web application which is integrate with it

## Used Naive Bayes classifier
As this is text classification application used Naive Bayes classifier for train the model
There are thre Naive Bayes classifiers I tested
* Multinomial Naive Bayes Classifier
* Gaussian Naive Bayes Calssifier
* Bernouli Naive Bayes Calssifier

## Compared all three classifiers with its performance metrics
### Then chose the MultiNomial Naive Bayes Classifier as it has 1.0 precision

##  EDA
EDA process has done with my own function, including:
* Lowercase the words
* Removing punctuation marks
* Remooving commonly used words which are not affect the performance of the model

## Web Application
Web application is created using Streamlit. Simple UI was created for ease of use of everyone.

## To use the appplication on your machine follow the below steps
* Download the repository
* Run this command in terminal (Make sure you have internet connection)
```
pip install -r requirements.txt
```
* Then in terminal you can simply use following command to use the application.
```
streamlit run app.py
```
* You can enter email text and predict for spam
