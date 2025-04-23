
---
---

<p align="center">
  <img src="./BEDA_logo3.png" alt="BEDA Logo" width="280"/>
  <h2 align="center"><i>Get it done the BEDA way</i></h2>
</p>

---

### 🔗 Navigation  
[🏠 Home](./index.md) | [📈 R Project](https://github.com/kochezz/002-house-price-prediction-R) | [📊 Python Project](https://kochezz.github.io/001-house-price-prediction-python/) | [📧 Contact](mailto:wphiri@beda.ie)

---

# 🏡 House Price Prediction using Multiple Linear Regression (Python)

[![Python](https://img.shields.io/badge/Built%20With-Python-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()
[![Data](https://img.shields.io/badge/Data-Cleaned-lightgrey)]()

---

## 📘 Project Overview

This project builds a **Multiple Linear Regression** model in **Python** to predict the **selling price** of houses based on:

- Carpet area (in square feet)
- Distance from the nearest metro station (in km)
- Number of schools within 2 km

---

## 📂 Repository Structure

```
FPM_Assignment_PY/
├── dashboards/
├── data/
├── environment/
├── models/
├── notebooks/
├── reports/
├── src/
└── README.md
```

---

## 📊 Model Summary

- **Model Type:** Multiple Linear Regression
- **R²:** 0.808
- **Adjusted R²:** 0.805
- **Train RMSE:** 1.700
- **Test RMSE:** 2.242

---

## 🔍 Diagnostics Summary

| Check                   | Result                         |
|------------------------|--------------------------------|
| Multicollinearity      | No (VIF < 5 for all variables) |
| Influential Points     | 8 removed (Cook’s Distance)    |
| Normality of Residuals | Slight deviation               |
| Homoscedasticity       | ✅ Verified via residual plots  |

---

## 🚀 Deployment

- **Streamlit App** is live at:  
  👉 [https://01-beda-house-price-prediction.streamlit.app/](https://01-beda-house-price-prediction.streamlit.app/)

- Features:
  - Manual input with sliders
  - Bulk CSV upload
  - Model trained on cleaned & validated dataset

---

## 📬 Contact

Business Enterprise Data Architecture (BEDA)  
📩 [wphiri@beda.ie](mailto:wphiri@beda.ie)  
🔗 [LinkedIn – William Phiri](https://www.linkedin.com/in/william-phiri-866b8443/)

---
