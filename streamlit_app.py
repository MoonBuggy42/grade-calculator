import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title('🥇Grade Calculator')

# --- Sidebar ---
with st.sidebar:
    st.subheader("Previous Outcomes")

    num_outcomes = st.slider("Number of Outcomes in Semester", 1, 5, 3)

    # Outcome labels
    outcome_labels = [f"Outcome {i+1}" for i in range(num_outcomes)]
    outcome_options = ["Excellent", "High", "Standard", "Partial", "Limited"]

    # Create a dictionary to store selections
    outcome_data = {}

    for label in outcome_labels:
        outcome_data[label] = st.selectbox(f"Enter {label}", outcome_options)

    # Convert to DataFrame
    df_outcomes = pd.DataFrame.from_dict(outcome_data, orient='index', columns=["Level"])

st.write("### 📊 Selected Outcomes")
st.dataframe(df_outcomes)
