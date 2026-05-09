import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title('🥇Grade Calculator')
with st.sidebar:
  st.subheader("Previous Outcomes")
  num_outcomes = st.slider("Number of Outcomes in Semester", 1, 10, 5)
  for x in range(num_outcomes):
    st.write("hi")
    
