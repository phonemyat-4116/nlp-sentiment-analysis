import streamlit as st
import pandas as pd
import numpy as np

st.write("hello world")
x = st.text_input("Write Something")

st.write(f"Hello : {x}")

data = pd.read_csv("Reviews.csv")
st.write(data.head(100))

chart_data = pd.DataFrame(np.random.randn(20, 3), 
                          columns=["a", "b", "c"])

print(chart_data)

st.bar_chart(chart_data)
st.line_chart(chart_data)
