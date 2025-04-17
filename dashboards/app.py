
import streamlit as st
import pandas as pd
import joblib
import os
from PIL import Image

# Set up page config
st.set_page_config(
    page_title="House Price Prediction | BEDA",
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Load and display logo
logo_path = "BEDA logo2.png"
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=150)

# Title and branding
st.markdown(
    "<h1 style='color:#ffffff;'>🏠 House Price Prediction App</h1>"
    "<h4 style='color:#cccccc;'>Business Enterprise Data Architecture (BEDA)</h4>"
    "<h5 style='color:#999999;'>Get it done the BEDA way</h5><br>",
    unsafe_allow_html=True
)

# Load model
MODEL_PATH = os.path.join("models", "house_price_model.pkl")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# User input section
st.subheader("🏠 Enter Property Details")

area = st.number_input("Carpet Area (sq. ft.)", min_value=200, max_value=10000, value=1200)
distance = st.number_input("Distance to Metro Station (km)", min_value=0.0, max_value=50.0, value=2.5)
schools = st.number_input("Number of Schools Nearby", min_value=0, max_value=20, value=3)

if st.button("🔍 Predict Selling Price"):
    input_df = pd.DataFrame([[area, distance, schools]], columns=["area", "distance", "schools"])
    prediction = model.predict(input_df)[0]
    st.success(f"💰 Estimated Selling Price: **{prediction:.2f} million Rs**")

# Divider
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
    "<center><small style='color:gray;'>© 2024 Business Enterprise Data Architecture (BEDA) • All rights reserved.</small></center>",
    unsafe_allow_html=True
)
