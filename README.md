# 🏠 House Price Prediction Assignment

This project uses a real estate dataset to build a multiple linear regression (MLR) model that predicts the selling price of houses (in million Rs) based on several predictors. The data consists of 198 rows and 5 columns containing the following information:
- **Selling Price** (in million Rs)
- **Carpet Area** (in square feet)
- **Distance from Nearest Metro Station** (in kilometers)
- **Number of Schools Within 2 km** of the house


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
## 📊 Analysis Process & Interpretations

| **Step**                         | **Description**                                      | **Key Metrics/Visuals**                  | **Interpretation Notes**                                      |
|----------------------------------|------------------------------------------------------|-------------------------------------------|----------------------------------------------------------------|
| **1. Data Check**                | Import data and examine structure                    | `.info()`, `.head()`                      | Ensure correct data types and no missing values                |
| **2. Data Split**                | Train-test split (80/20)                             | `train_test_split()`                      | Prevent data leakage, ensure fair model evaluation             |
| **3. Model Building**            | Fit MLR model using training set                     | `.summary()` (statsmodels)                | Review model fit and statistical output                        |
| **4. Coefficient Analysis**      | Identify significant variables                       | p-values < 0.05                           | Only significant variables should be interpreted               |
| **5. Model Fit**                 | Evaluate R² and Adjusted R²                          | R², Adj R²                                | How much variance in selling price is explained                |
| **6. Multicollinearity**         | Check with VIF                                       | `variance_inflation_factor()`             | VIF > 5–10 suggests strong multicollinearity                   |
| **7. Influential Observations**  | Identify outliers affecting model                    | Leverage plots, Cook’s Distance           | Influential points may distort regression                     |
| **8. Normality of Errors**       | Check distribution of residuals                      | Q-Q Plot, Shapiro-Wilk test               | Model assumes residuals are normally distributed               |
| **9. Heteroscedasticity**        | Test variance of residuals across predictors         | Residual vs. fitted/predictor plots       | Look for "funnel" shape; should ideally be constant            |
| **10. RMSE Calculation**         | Calculate error on both Train and Test sets          | RMSE (scikit-learn)                       | Lower RMSE → better model accuracy and generalization          |

---
## 🤝 Collaboration & Contributions

Contributions are Welcome!

If you'd like to suggest changes, improve code, or add new features:

1. Fork the repository
2. Create a new branch (`feature/my-new-feature`)
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

For significant changes, please open an issue first to discuss what you'd like to change.

Let's collaborate and grow together 🚀

---
## 📜 License

This project is licensed under the MIT License.  
You are free to use, modify, and distribute it with attribution.

---
## 👤 Author

**William Chenecho Phiri**  
📧 [chenechoz@gmail.com](mailto:chenechoz@gmail.com)  
🌐 [GitHub Profile](https://github.com/kochezz) 

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

## 🚀 How to Run the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/FPM_Assignment_PY.git
   cd FPM_Assignment_PY

conda env create -f environment/environment.yml
conda activate ds-env

---

