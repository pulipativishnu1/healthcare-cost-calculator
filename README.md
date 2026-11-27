Healthcare Cost Calculator

Project Overview

An AI/ML-based application that predicts annual health insurance charges using personal information.

Input Features

- Age
- BMI
- Smoking Status
- Region

Technologies

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Streamlit

Team Members

1. P.Sai Vishnu Prasad
2. B.Gnaneswar
3. B.Jhansi

Project Objective

To develop an interactive healthcare cost calculator that predicts annual insurance charges and displays visual cost breakdowns.

## Live App
https://healthcare-cost-calculator-ucbuy97qytinpv79hzgbsv.streamlit.app

## Dataset
Medical Cost Personal Dataset (insurance.csv), 1,338 records with age, BMI, smoker, region and charges.

## Model
- Linear Regression: R2 = 0.78
- Random Forest: R2 = 0.87 (used in the app)

## Features of the App
- Sliders for age and BMI, options for smoker and region
- Predicted annual insurance cost
- Charts: smoker vs non-smoker, cost by age, factor importance

## How to Run Locally
pip install -r requirements.txt
python -m streamlit run app.py
