import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Search for Happines")
option_x = st.selectbox("Select for X axis", ("GDP", "Happines", "Generosity"))
option_y = st.selectbox("Select for Y axis", ("GDP", "Happines", "Generosity"))

st.subheader(f"{option_x} and {option_y}")

# getting data
data_x = [43, 23, 55]
data_y = [11, 22, 33]

figure = px.line(x=data_x, y=data_y, labels={"x": option_x, "y": option_y})

st.plotly_chart(figure)
