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

TEAM MEMBERS AND COLLABORATIONS
This project was collaboratively developed by three team members.


Member 1 – Data Collection and Preprocessing
Dataset collection and understanding.
Data cleaning and preprocessing.
Exploratory Data Analysis.
Feature preparation.


Member 2 – Machine Learning Development
Algorithm selection.
Model training and testing.
Model evaluation.
Saving trained model and prediction columns.


Member 3 – Application Development and Integration
Application development using Python.
Integration of the trained ML model.
User input and prediction functionality.
Application testing and documentation.

Team Collaboration
All three members collaborated in developing, testing, and completing the Healthcare Cost Calculator project.

Dataset Collection and Preprocessing

Module 1 – Data Preprocessing and Exploratory Data Analysis

Objective

To collect, understand, clean and preprocess the healthcare insurance dataset before applying machine learning algorithms.

Dataset Description

The dataset contains the following attributes:

- Age
- Sex
- BMI
- Children
- Smoking Status
- Region
- Insurance Charges

Tasks Completed

1. Dataset collection.
2. Dataset exploration.
3. Missing value checking.
4. Duplicate record identification and removal.
5. Data cleaning.
6. Categorical data standardization.
7. Feature selection.
8. Exploratory Data Analysis.
9. Data visualization.

Selected Features

- Age
- BMI
- Smoking Status
- Region

Target Variable: Insurance Charges

Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

Output

The cleaned dataset and EDA visualizations are prepared for the machine learning model training module.

Team Contribution

Member 1: Dataset Collection, Data Cleaning, Preprocessing and EDA.


