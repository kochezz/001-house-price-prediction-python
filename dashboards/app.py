
import streamlit as st
import pandas as pd
import joblib


# Page config
st.set_page_config(page_title="House Price Prediction", layout="centered")

# Title
st.title("🏠 House Price Prediction App")
st.markdown("Upload new house data and predict selling prices using the trained model.")

# Sidebar
st.sidebar.header("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Load model from absolute path
@st.cache_resource
def load_model():
    return joblib.load("C:/Users/willi/GitHub/FPM_Assignment_PY/models/house_price_model.pkl")

model = load_model()
formula = "price ~ area + distance + schools"
formula_features = formula.replace("price ~", "")

# Predict and display
if uploaded_file:
    try:
        new_data = pd.read_csv(uploaded_file)
        st.write("📋 Preview of uploaded data:")
        st.dataframe(new_data.head())

        # Create feature matrix
        X_new = new_data[["area", "distance", "schools"]]

        # Predict prices
        predictions = model.predict(X_new)
        new_data["Predicted Price (million Rs)"] = predictions

        st.success("✅ Predictions generated successfully!")
        st.dataframe(new_data)

        # Download button
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
    st.info("👈 Upload a file to begin.")
