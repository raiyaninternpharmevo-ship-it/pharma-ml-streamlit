import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🧪 Drug Approval Prediction System")
st.write("Machine Learning model for Pharma Industry")

toxicity = st.slider("Toxicity Level (0–10)", 0, 10)
trial = st.slider("Clinical Trial Score (0–100)", 0, 100)
side = st.slider("Side Effects Severity (0–10)", 0, 10)
eff = st.slider("Efficacy Score (0–100)", 0, 100)

if st.button("Predict Drug Approval"):
    prediction = model.predict([[toxicity, trial, side, eff]])
    if prediction[0] == 1:
        st.success("✅ Drug is APPROVED")
    else:
        st.error("❌ Drug is NOT APPROVED")
