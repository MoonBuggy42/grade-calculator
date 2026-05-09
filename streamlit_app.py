import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title('🥇Grade Calculator')
with st.sidebar:
  st.subheader("Previous Outcomes")
  num_outcomes = st.slider("Number of Outcomes in Semester", 1, 5, 3)
  if num_outcomes == 1:
    out_1 = st.selectbox("Enter Outcome 1", ("Excellent", "High", "Standard", "Partial", "Limited"))
    
