import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# UI
st.title("📧 Email Spam Classifier")
st.write("Enter a message to check if it's spam or not.")

user_input = st.text_area("Enter email text:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)

        if prediction[0] == 1:
            st.error("🚨 This message is **SPAM**.")
        else:
            st.success("✅ This message is **NOT SPAM**.")
