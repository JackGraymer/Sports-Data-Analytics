import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")
    
df = pd.read_csv("data/maps_statistics.csv")
st.line_chart(df)