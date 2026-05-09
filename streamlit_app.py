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
    st.subheader("Final Grade")
    final_grade = st.selectbox("Desired Final Grade", outcome_options)
with st.expander("Data Versions"):
    # Mapping text → numeric values
    level_map = {
        "Excellent": 5,
        "High": 4,
        "Standard": 3,
        "Partial": 2,
        "Limited": 1
    }
    
    # Create numeric version of the dataframe
    df_outcomes_numeric = df_outcomes.copy()
    df_outcomes_numeric["Value"] = df_outcomes_numeric["Level"].map(level_map)
    
    st.write("### 📊 Selected Outcomes")
    st.dataframe(df_outcomes)
    
    st.write("### 🔢 Numeric Outcome Values")
    st.dataframe(df_outcomes_numeric)

total = df_outcomes_numeric["Value"].sum()
average = int(total / num_outcomes)

value_to_grade = {
    5: "Excellent",
    4: "High",
    3: "Standard",
    2: "Partial",
    1: "Limited"
}

final_grade = value_to_grade.get(average, "Invalid")

st.write("### 📈 Average Score:", round(average, 2))
st.write("### 🏅 Current Grade:", final_grade)

    
