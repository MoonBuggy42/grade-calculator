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
  elif num_outcomes == 2:
    out_1 = st.selectbox("Enter Outcome 1", ("Excellent", "High", "Standard", "Partial", "Limited"))
    out_2 = st.selectbox("Enter Outcome 2", ("Excellent", "High", "Standard", "Partial", "Limited"))
  elif num_outcomes == 3:
    out_1 = st.selectbox("Enter Outcome 1", ("Excellent", "High", "Standard", "Partial", "Limited"))
    out_2 = st.selectbox("Enter Outcome 2", ("Excellent", "High", "Standard", "Partial", "Limited"))
    out_3 = st.selectbox("Enter Outcome 3", ("Excellent", "High", "Standard", "Partial", "Limited"))
  elif num_outcomes == 4:
    out_1 = st.selectbox("Enter Outcome 1", ("Excellent", "High", "Standard", "Partial", "Limited"))
    out_2 = st.selectbox("Enter Outcome 2", ("Excellent", "High", "Standard", "Partial", "Limited"))
    out_3 = st.selectbox("Enter Outcome 3", ("Excellent", "High", "Standard", "Partial", "Limited")
    out_4 = st.selectbox("Enter Outcome 4", ("Excellent", "High", "Standard", "Partial", "Limited")
  else:
    out_1 = st.selectbox("Enter Outcome 1", ("Excellent", "High", "Standard", "Partial", "Limited"))
    out_2 = st.selectbox("Enter Outcome 2", ("Excellent", "High", "Standard", "Partial", "Limited"))
    out_3 = st.selectbox("Enter Outcome 3", ("Excellent", "High", "Standard", "Partial", "Limited")
    out_4 = st.selectbox("Enter Outcome 4", ("Excellent", "High", "Standard", "Partial", "Limited"))
    out_5 = st.selectbox("Enter Outcome 5", ("Excellent", "High", "Standard", "Partial", "Limited")
