# 📨 SMS Spam Classifier using Machine Learning

A machine learning-powered web application that classifies SMS or email messages as **Spam** or **Not Spam** in real time.  
Built using **Python, Streamlit, and NLP**, and deployed seamlessly on **Render Cloud Platform**.

---

## 🌟 Project Overview

With the rapid growth of digital communication, spam detection has become essential to safeguard users from unwanted or malicious messages.  
This project demonstrates how Natural Language Processing (NLP) and Machine Learning can be combined to automate spam filtering with high accuracy.

Users can simply type or paste a message into the app, and the classifier instantly predicts whether it’s **Spam** or **Not Spam** — powered by a trained ensemble model.

---

## 🧠 How It Works

1. **Text Preprocessing (NLP)**  
   - Converts text to lowercase  
   - Removes stopwords, punctuation, and special characters  
   - Applies stemming using PorterStemmer  

2. **Feature Extraction**  
   - Uses **TF-IDF Vectorization** to transform text into numerical form  

3. **Model Training**  
   - Trained on the classic **SMS Spam Collection Dataset**  
   - Combines multiple classifiers (`Naive Bayes`, `SVC`, `Extra Trees`, and `Random Forest`) using **Stacking Ensemble Learning**  

4. **Deployment**  
   - The final model is integrated into a **Streamlit** app  
   - Hosted publicly on **Render Cloud Platform**

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python |
| **Frontend** | Streamlit |
| **ML Framework** | Scikit-learn |
| **Text Processing** | NLTK |
| **Deployment** | Render Cloud Platform |

---

## 🚀 Features

- Real-time SMS spam classification  
- Clean, interactive Streamlit interface  
- Trained with TF-IDF and Ensemble Learning  
- High accuracy and precision on test data  
- Cloud-deployed for public access  

---

## 📂 Project Structure
sms-spam-classifier/
│
├── app.py # Streamlit web app
├── sms-spam-detection.ipynb # Model training notebook
├── vectorizer.pkl # Saved TF-IDF vectorizer
├── model.pkl # Saved trained model (Stacking Classifier)
├── spam.csv # Dataset used for training
└── requirements.txt # Python dependencies



---

## ⚙️ How to Run Locally

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

## 🌐 Deployment

This app is deployed on **Render Cloud Platform**, making it accessible online for real-time spam classification.  
Render handles the backend environment setup, allowing for smooth and continuous deployment directly from this GitHub repository.

---

## 📊 Example Predictions

| **Input Message** | **Prediction** |
|--------------------|----------------|
| "Congratulations! You’ve won ₹10,000. Click to claim your prize!" | 🧨 Spam |
| "Hey, are we still meeting at 7 for dinner?" | ✅ Not Spam |


## 🧾 License

This project is open-source under the **MIT License**.  
You are free to **use, modify, and distribute** it with proper attribution.



---

Would you like me to customize it further with your **Render app link** and **LinkedIn profile URL** before finalizing it for upload?

