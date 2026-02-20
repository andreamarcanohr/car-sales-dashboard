import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Car Sales Advertisement Dashboard")

# Load data
df = pd.read_csv('vehicles_us.csv')

df = df.dropna(subset=['price', 'odometer'])

st.write("Dataset Preview")
st.dataframe(df.head())

# Checkbox filter
show_high_price = st.checkbox("Show only vehicles above $20,000")

if show_high_price:
    df = df[df['price'] > 20000]

# Histogram
st.subheader("Price Distribution of Vehicles")
fig1 = px.histogram(
    df[df['price'] < 100000],
    x='price',
    nbins=50
)
st.plotly_chart(fig1)

# Scatter Plot
st.subheader("Odometer vs Price by Fuel Type")
fig2 = px.scatter(
    df,
    x='odometer',
    y='price',
    color='fuel',
    opacity=0.6
)
st.plotly_chart(fig2)
