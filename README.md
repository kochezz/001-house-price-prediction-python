
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

The dataset contains **198 observations** and 5 variables.

The Project aims to;
- Predict house prices in millions of Rs
- Input values via a clean Streamlit UI with the option to upload a csv file.
- Model trained using `scikit-learn` Linear Regression
- Built with reproducibility and scalability in mind
  
---

## 📂 Repository Structure

```
FPM_Assignment_PY/
├── dashboards/                 # Streamlit app
│   └── app.py
├── data/
│   ├── raw/
│   └── processed/
├── environment/               # Conda & pip environment files
├── models/                    # Pickled regression model
├── notebooks/                 # EDA, model building, evaluation
├── reports/                   # Text and PDF summaries
├── src/                       # Reusable Python scripts
└── README.md
```

---

## 📊 Final Model Summary

- **Model Type:** Multiple Linear Regression
- **R²:** 0.808 (after removing influential points)
- **Adjusted R²:** 0.805
- **Train RMSE:** 1.700
- **Test RMSE:** 2.242

**Significant Predictors:**  
✅ `area`  
✅ `distance`  
❌ `schools` (became insignificant after removing influential points)

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

- A **Streamlit dashboard** was developed for interactive predictions
- Users can:
  - Manually enter values via sliders
  - Upload CSVs for batch prediction
- Deployment ready for local and cloud hosting

---

## 📬 Contact

Developed by **Business Enterprise Data Architecture (BEDA)**  
📩 Email: [wphiri@beda.ie](mailto:wphiri@beda.ie)  
🔗 LinkedIn: [William Phiri](https://www.linkedin.com/in/william-phiri-866b8443/)  
🧭 _"Get it done the BEDA way"_

---

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
