# 🏠 House Price Prediction Assignment

This project uses a real estate dataset to build a multiple linear regression (MLR) model that predicts the selling price of houses (in million Rs) based on several predictors. The data consists of 198 rows and 5 columns containing the following information:
- **Selling Price** (in million Rs)
- **Carpet Area** (in square feet)
- **Distance from Nearest Metro Station** (in kilometers)
- **Number of Schools Within 2 km** of the house
- *(Any additional identifier column if available)*

---

## 📋 Objectives / Questions Addressed

1. **Data Import & Structure Check**  
   - Import the House Price data and examine its structure.

2. **Data Splitting**  
   - Split the data into Training (80%) and Testing (20%) datasets.

3. **Model Building**  
   - Build a regression model on the training data to estimate the selling price of a house.

4. **Variable Significance & Interpretation**  
   - Identify significant predictors and interpret their regression coefficients.

5. **Model Fit Metrics**  
   - Report the R² and Adjusted R² of the model along with their interpretations.

6. **Multicollinearity Assessment**  
   - Check for multicollinearity (e.g., using VIF) and perform necessary steps to address it.

7. **Influential Observations**  
   - Identify any influential observations that might disproportionately affect the model.

8. **Error Normality**  
   - Assess if the model residuals (errors) follow a normal distribution.

9. **Heteroscedasticity Check**  
   - Evaluate for heteroscedasticity by plotting residuals versus the predictors.

10. **Model Performance**  
    - Calculate the Root Mean Squared Error (RMSE) for both Training and Testing datasets.

---

## 🔧 Tools & Technologies

- **Python** (3.x) with key libraries:
  - **pandas** & **numpy** for data manipulation
  - **matplotlib** & **seaborn** for visualizations
  - **scikit-learn** for data splitting and evaluation
  - **statsmodels** & **patsy** for building regression models and performing diagnostics
  - Additional packages for EDA and statistical tests if required

- The project is fully reproducible using a provided Conda environment with an `environment.yml` file.

---

## 🗂️ Project Structure

```plaintext
HousePricePrediction/
├── data/
│   ├── raw/                # Original house price data file
│   └── processed/          # Cleaned and processed datasets
├── notebooks/              # Jupyter notebooks for EDA and modeling
├── src/                    # Source scripts for data cleaning, model training, and utilities
│   ├── data_prep.py        # Data preprocessing functions
│   ├── train_model.py      # Script to train the regression model
│   └── utils.py            # Helper functions
├── models/                 # Saved model objects (e.g., pickle files)
├── reports/                # Generated reports and figures (e.g., residual plots)
├── environment/            # Environment configuration files
│   ├── environment.yml     # Conda environment file
│   └── requirements.txt    # pip requirements file (if needed)
├── README.md               # Project overview and instructions
└── main.py                 # Main script to run the model (optional)


