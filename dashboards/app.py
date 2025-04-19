
import streamlit as st
import pandas as pd
import joblib
import os
from PIL import Image

# Page config
st.set_page_config(
    page_title="House Price Predictor | BEDA",
    page_icon="🏠",
    layout="centered"
)

# Load logo
logo_path = "BEDA logo2.png"
if os.path.exists(logo_path):
    st.image(logo_path, width=150)

# Title
st.markdown(
    "<h1 style='color:#ffffff;'>🏠 House Price Prediction App</h1>"
    "<h4 style='color:#cccccc;'>Business Enterprise Data Architecture (BEDA)</h4>"
    "<h5 style='color:#999999;'>Get it done the BEDA way</h5><br>",
    unsafe_allow_html=True
)

# Load model
@st.cache_resource
def load_model():
    return joblib.load(os.path.join("models", "house_price_model.pkl"))

model = load_model()

# Tabs for prediction methods
tab1, tab2 = st.tabs(["📄 Predict via CSV", "🔢 Predict a Single House"])

with tab1:
    st.subheader("📄 Upload CSV File for Batch Prediction")
    uploaded_file = st.file_uploader("Upload a CSV file with columns: area, distance, schools", type="csv")
    
    if uploaded_file:
        try:
            input_data = pd.read_csv(uploaded_file)
            st.dataframe(input_data)

            preds = model.predict(input_data[["area", "distance", "schools"]])
            input_data["Predicted Price (million Rs)"] = preds

            st.success("✅ Predictions complete.")
            st.dataframe(input_data)

            csv_download = input_data.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Results", csv_download, file_name="house_predictions.csv")

        except Exception as e:
            st.error(f"❌ Could not process file: {e}")

with tab2:
    st.subheader("🔢 Enter Property Details")

    area = st.number_input("Carpet Area (sq ft)", min_value=100, max_value=10000, value=1200)
    distance = st.number_input("Distance to Metro (km)", min_value=0.0, max_value=100.0, value=3.0)
    schools = st.number_input("Number of Schools Nearby", min_value=0, max_value=20, value=3)

    if st.button("🔍 Predict"):
        input_df = pd.DataFrame([[area, distance, schools]], columns=["area", "distance", "schools"])
        pred = model.predict(input_df)[0]
        st.success(f"💰 Predicted Price: {pred:.2f} million Rs")

# Contact Form
st.markdown("---")
st.subheader("📬 Contact Us")

contact_form = """
<form action="https://formsubmit.co/wphiri@beda.ie" method="POST">
    <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 8px;"><br><br>
    <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 8px;"><br><br>
    <textarea name="message" placeholder="Your message here..." rows="4" required style="width: 100%; padding: 8px;"></textarea><br><br>
    <button type="submit" style="background-color: #404040; color: white; padding: 10px 20px; border: none;">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Footer
st.markdown(
    "<hr style='margin-top: 50px;'>"
    "<center><small style='color:gray;'>© 2024 Business Enterprise Data Architecture (BEDA)</small></center>",
    unsafe_allow_html=True
)
