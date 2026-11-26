import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Healthcare Cost Calculator", layout="centered")

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

def predict(age, bmi, smoker, region):
    row = pd.DataFrame([{"age": age, "bmi": bmi, "smoker": smoker, "region": region}])
    row = pd.get_dummies(row)
    row = row.reindex(columns=columns, fill_value=0)
    return model.predict(row)[0]

st.title("Healthcare Cost Calculator")
st.write("Estimate your annual health insurance charges.")

# Inputs
age = st.slider("Age", 18, 64, 30)
bmi = st.slider("BMI", 15.0, 50.0, 25.0, 0.1)
smoker = st.radio("Smoker?", ["no", "yes"], horizontal=True)
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Prediction
cost = predict(age, bmi, smoker, region)
st.metric("Estimated annual cost", f"${cost:,.0f}")

# Chart 1: smoker vs non-smoker
st.subheader("Smoker vs non-smoker (same age, BMI, region)")
compare = pd.DataFrame(
    {"Cost": [predict(age, bmi, "no", region), predict(age, bmi, "yes", region)]},
    index=["Non-smoker", "Smoker"],
)
st.bar_chart(compare)

# Chart 2: cost across ages
st.subheader("How cost changes with age")
ages = list(range(18, 65))
by_age = pd.DataFrame(
    {"Cost": [predict(a, bmi, smoker, region) for a in ages]}, index=ages
)
st.line_chart(by_age)

# Chart 3: which factors matter most
st.subheader("Which factors matter most")
importance = pd.Series(model.feature_importances_, index=columns).sort_values()
st.bar_chart(importance)

st.caption("Estimates come from a model trained on sample data. Not real insurance quotes.")