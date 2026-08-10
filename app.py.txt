import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("House Price Estimator")

df = pd.read_csv("house_prices.csv")
X = df[['Area', 'Bedrooms']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

area = st.number_input("Area (sqft)", 500, 5000, 1200)
bedrooms = st.number_input("Bedrooms", 1, 5, 2)

if st.button("Predict Price"):
    price = model.predict([[area, bedrooms]])
    st.success(f"Estimated Price: ₹{price[0]:,.0f}")