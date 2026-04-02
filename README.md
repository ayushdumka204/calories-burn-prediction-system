# 🏃‍♂️ Calorie Burn Prediction System

## 📌 Project Overview
This project is a Machine Learning-based solution designed to estimate the number of calories burned during physical activity based on specific parameters (such as age, weight, heart rate, and duration). The main objective is to make fitness tracking more data-driven and user-friendly.

## 📁 Repository Structure
- **Dataset/**: Contains the original CSV files (Exercise and Calories) used for training and testing.
- **ML CODE.ipynb**: Jupyter Notebook featuring Data Cleaning, Exploratory Data Analysis (EDA), Feature Engineering, and Model Building.
- **app.py**: Source code for the web application (Streamlit/Flask-based) providing the user interface.
- **pipeline.pkl**: The serialized trained ML model file used for generating real-time predictions.
- **ML Report & Presentation**: Detailed project documentation, methodology, and presentation (PPT) files.

## ✨ Features
- **Multiple Model Support:** Comparisons between Linear Regression, Random Forest, SVR, and XGBoost models to ensure the best accuracy.
- **Interactive Web UI:** A user-friendly dashboard implemented via `app.py`.
- **Data Insights:** Visualizations like Heatmaps and Scatter plots to demonstrate the impact of workout duration and heart rate on calorie expenditure.
- **Pre-processing Pipeline:** A robust setup to automatically handle raw data transformations.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** - `Pandas` & `NumPy` (Data Manipulation)
  - `Scikit-Learn` & `XGBoost` (Machine Learning)
  - `Matplotlib` & `Seaborn` (Data Visualization)
- **Web Framework:** Flask / Streamlit (for UI implementation)

## 🚀 How to Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ayushdumka204/calories-burn-prediction-system.git](https://github.com/ayushdumka204/calories-burn-prediction-system.git)