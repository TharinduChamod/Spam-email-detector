# running app with imported model
import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

# Load the TFIDF Vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Set the title of the Streamlit page
st.title("Spam e-mail predictor")

# Get the input
text = st.text_area("Enter e-mail message")

# Prerpocess data using same function that used for model training
def process_email(text):

  # Remove the punctuation
  no_punct = [char for char in text if char not in string.punctuation]
  no_punct = ''.join(no_punct)

  # Remove the stopwords
  clean_words = [word for word in no_punct.split() if word.lower() not in stopwords.words('english')]
  clean_words = " ".join(clean_words)

  # Return the list of clean text words
  return clean_words

if(st.button('Predict')):
    # Transform input email
    transformed_email = process_email(text)

    # Vectorize the text
    vectorized_text = tfidf.transform([transformed_email])

    # Predict the value of given inpput
    prediction = model.predict(vectorized_text)[0]

    if(prediction==1):
        st.header("This is spam e-mail")
    else:
        st.header('This is non-spam e-mail')