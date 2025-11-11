# SMS Spam Classifier using Machine Learning

A machine learning-powered web application that classifies SMS or email messages as **Spam** or **Not Spam** in real time.  
Built using **Python, Streamlit, and NLP**, and deployed seamlessly on **Render Cloud Platform**.



  - ##  Project Overview
    content: |
      With the rapid growth of digital communication, spam detection has become essential to protect users from unwanted or malicious content.
      This project demonstrates how Natural Language Processing (NLP) and Machine Learning can be integrated to automate spam filtering with high accuracy.

      Users can input any message, and the system predicts whether it is Spam or Not Spam using a trained Stacking Ensemble Model.

  - ## System Architecture
    content: |
      ```mermaid
      flowchart TD
          A[User Input Message] --> B[Text Preprocessing]
          B --> C[TF-IDF Vectorization]
          C --> D[Trained Ensemble Model]
          D --> E[Prediction: Spam or Not Spam]
          E --> F[Streamlit Web Interface]
          F --> G[Render Cloud Deployment]
      ```

  - ## How It Works
    content: |
      1. **Text Preprocessing**
         - Converts all text to lowercase
         - Removes stopwords, punctuation, and special characters
         - Applies stemming using the Porter Stemmer

      2. **Feature Extraction**
         - Transforms processed text into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency)

      3. **Model Training**
         - Trained on the SMS Spam Collection Dataset
         - Uses a Stacking Ensemble of multiple classifiers:
           - Naive Bayes
           - Support Vector Classifier (SVC)
           - Extra Trees Classifier
           - Random Forest Classifier

      4. **Deployment**
         - The model and TF-IDF vectorizer are integrated into a Streamlit application
         - Deployed on Render Cloud Platform for public access

  - ## Tech Stack
    table:
      headers: ["Component", "Technology"]
      rows:
        - ["Programming Language", "Python"]
        - ["Frontend Framework", "Streamlit"]
        - ["Machine Learning", "Scikit-learn"]
        - ["Text Processing", "NLTK"]
        - ["Deployment", "Render Cloud Platform"]

  - ## Features
    list:
      - "Real-time SMS spam detection"
      - "Lightweight and interactive user interface"
      - "Ensemble model for high accuracy"
      - "Deployed and accessible via web"
      - "Easy to extend for email or other message classification"

  - ## Project Structure
    content: |
      ```text
      sms-spam-classifier/
      │
      ├── app.py                     # Streamlit application
      ├── sms-spam-detection.ipynb   # Model training and experimentation
      ├── vectorizer.pkl             # Saved TF-IDF vectorizer
      ├── model.pkl                  # Trained ensemble model
      ├── spam.csv                   # Dataset used for model training
      └── requirements.txt           # Dependencies for the project
      ```

  - ## How to Run Locally
    content: |
      ```bash
      # Clone the repository
      git clone https://github.com/your-username/sms-spam-classifier.git

      # Navigate into the directory
      cd sms-spam-classifier

      # Install dependencies
      pip install -r requirements.txt

      # Run the Streamlit app
      streamlit run app.py
      ```

      Then open the displayed local URL in your browser.


