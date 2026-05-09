import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title('🥇Grade Calculator')

st.subheader("Previous Outcomes")
st.slider("Number of Outcomes in Semester", 1, 10, 5)
