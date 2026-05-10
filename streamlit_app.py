import streamlit as st
import pandas as pd
import itertools
import math

st.title('🥇Grade Calculator')

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.subheader("Previous Outcomes")

    num_outcomes = st.slider("Number of Outcomes in Semester", 1, 5, 3)

    # Outcome labels
    outcome_labels = [f"Outcome {i+1}" for i in range(num_outcomes)]
    outcome_options = ["Excellent", "High", "Standard", "Partial", "Limited"]

    # Store selections
    outcome_data = {}
    for label in outcome_labels:
        outcome_data[label] = st.selectbox(f"Enter {label}", outcome_options)

    # Convert to DataFrame
    df_outcomes = pd.DataFrame.from_dict(outcome_data, orient='index', columns=["Level"])

    st.subheader("Final Grade Goal")
    desired_grade = st.selectbox("Desired Final Grade", outcome_options)

    outcomes_left = st.slider("Number of Outcomes Left", 1, 5, 3)

# ---------------- DATA PROCESSING ----------------

# Mapping text → numeric values
level_map = {
    "Excellent": 5,
    "High": 4,
    "Standard": 3,
    "Partial": 2,
    "Limited": 1
}

# Reverse map
value_to_grade = {v: k for k, v in level_map.items()}

# Numeric version of the dataframe
df_outcomes_numeric = df_outcomes.copy()
df_outcomes_numeric["Value"] = df_outcomes_numeric["Level"].map(level_map)

# Show dataframes
with st.expander("Data Versions"):
    st.write("### 📊 Selected Outcomes")
    st.dataframe(df_outcomes)

    st.write("### 🔢 Numeric Outcome Values")
    st.dataframe(df_outcomes_numeric)

# ---------------- CURRENT GRADE ----------------

total = df_outcomes_numeric["Value"].sum()
average = total / num_outcomes
rounded = round(average)
current_grade = value_to_grade.get(rounded, "Invalid")

st.write("### 📈 Current Average Score:", round(average, 2))
st.write("### 🏅 Current Grade:", current_grade)

# ---------------- TARGET CALCULATION ----------------

target_value = level_map[desired_grade]

possible_values = list(level_map.values())

# Generate all combinations for remaining outcomes
all_combos = list(itertools.product(possible_values, repeat=outcomes_left))

valid_combos = []

current_total = df_outcomes_numeric["Value"].sum()
total_outcomes = num_outcomes + outcomes_left

for combo in all_combos:
    new_total = current_total + sum(combo)
    avg = new_total / total_outcomes
    rounded = round(avg)

    if rounded == target_value:
        valid_combos.append(combo)

# ---------------- DISPLAY RESULTS ----------------

st.subheader("🎯 Possible Ways to Reach Your Desired Grade")

if len(valid_combos) == 0:
    st.error("❌ No possible combinations can reach this grade.")
else:
    readable = [
        [value_to_grade[v] for v in combo]
        for combo in valid_combos
    ]

    df_valid = pd.DataFrame(
        readable,
        columns=[f"Outcome {i+1}" for i in range(outcomes_left)]
    )

    st.success(f"✅ Found {len(valid_combos)} possible combinations!")
    st.dataframe(df_valid)

