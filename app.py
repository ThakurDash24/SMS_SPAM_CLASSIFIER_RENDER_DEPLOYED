import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import os
import logging

# ========== Setup Logging ==========
logging.basicConfig(level=logging.INFO)

# ========== NLTK Data Setup ==========
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# New fix: handle missing 'punkt_tab' (required by newer NLTK)
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

ps = PorterStemmer()

# ========== Text Transformation Function ==========
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    # Keep only alphanumeric words
    y = [i for i in text if i.isalnum()]

    # Remove stopwords and punctuation
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]

    # Apply stemming
    y = [ps.stem(i) for i in y]

    return " ".join(y)

# ========== Safe Path Setup ==========
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VECT_PATH = os.path.join(BASE_DIR, 'vectorizer.pkl')
MODEL_PATH = os.path.join(BASE_DIR, 'model.pkl')

logging.info(f"BASE_DIR: {BASE_DIR}")
logging.info(f"Files in BASE_DIR: {os.listdir(BASE_DIR)}")

# ========== Load Pickle Files Safely ==========
try:
    with open(VECT_PATH, 'rb') as f:
        tfidf = pickle.load(f)
    logging.info(f"Vectorizer loaded from {VECT_PATH}")

    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    logging.info(f"Model loaded from {MODEL_PATH}")

except Exception as e:
    logging.exception(f"Error loading model/vectorizer: {e}")
    st.error("Failed to load model files. Please check server logs.")
    st.stop()

# ========== Streamlit App ==========
st.title(" Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    if not input_sms.strip():
        st.warning("Please enter a message to predict.")
    else:
        try:
            # 1. Preprocess
            transformed_sms = transform_text(input_sms)
            # 2. Vectorize
            vector_input = tfidf.transform([transformed_sms]).toarray()
            # 3. Predict
            result = model.predict(vector_input)[0]
            # 4. Display
            if result == 1:
                st.header("🚨 Spam")
            else:
                st.header(" Not Spam")
        except Exception as e:
            logging.exception(f"Prediction error: {e}")
            st.error(f"Error during prediction: {e}")
