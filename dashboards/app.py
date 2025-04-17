
import streamlit as st
import pandas as pd
import joblib
import os
from PIL import Image

# Set dark theme styling and page config
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

# Title and tagline
st.markdown(
    "<h1 style='color:#ffffff;'>🏠 House Price Prediction App</h1>"
    "<h4 style='color:#cccccc;'>Business Enterprise Data Architecture (BEDA)</h4>"
    "<h5 style='color:#999999;'>Get it done the BEDA way</h5><br>",
    unsafe_allow_html=True
)

# Sidebar file uploader
st.sidebar.header("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Load model
MODEL_PATH = os.path.join("models", "house_price_model.pkl")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# Main prediction workflow
if uploaded_file:
    try:
        new_data = pd.read_csv(uploaded_file)
        st.subheader("📋 Preview of Uploaded Data")
        st.dataframe(new_data)

        X_new = new_data[["area", "distance", "schools"]]
        predictions = model.predict(X_new)
        new_data["Predicted Price (million Rs)"] = predictions

        st.success("✅ Predictions generated successfully!")
        st.dataframe(new_data)

        csv = new_data.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Predictions as CSV",
            data=csv,
            file_name="predicted_house_prices.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
else:
    st.info("👈 Upload a CSV file to begin prediction.")

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
    "<center><small style='color:gray;'>© 2024 Business Enterprise Data Architecture (BEDA) • All rights reserved.</small></center>",
    unsafe_allow_html=True
)
