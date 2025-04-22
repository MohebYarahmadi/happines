import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Search for Happiness")
option_x = st.selectbox("Select for X axis", ("GDP", "Happiness", "Generosity"))
option_y = st.selectbox("Select for Y axis", ("GDP", "Happiness", "Generosity"))

st.subheader(f"{option_x} and {option_y}")

# Getting data
df = pd.read_csv('happy.csv')
data_x = df[option_x.lower()].squeeze()
data_y = df[option_y.lower()].squeeze()

figure = px.scatter(x=data_x, y=data_y, labels={"x": option_x, "y": option_y})
st.plotly_chart(figure)
