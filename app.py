import streamlit as st
import pandas as pd
from datetime import datetime
import hashlib
import random

st.set_page_config(page_title="Migrant Health Connect", page_icon="💊")

# In-memory database
if "workers" not in st.session_state:
    st.session_state.workers = []

st.title("💊 Migrant Health Connect – Prototype")

# Sidebar menu for roles
role = st.sidebar.radio("Login as", ["Worker", "Doctor", "Government"])

# ---------------- Worker Registration ----------------
if role == "Worker":
    st.header("👷 Worker Registration")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    if st.button("Register"):
        # Save record
        record = {"Name": name, "Age": age, "Gender": gender, "Date": datetime.now()}
        st.session_state.workers.append(record)

        # Blockchain hash demo
        hash_val = hashlib.sha256(f"{name}{age}{datetime.now()}".encode()).hexdigest()

        # AI demo
        risk = random.choice(["Low", "Medium", "High"])

        st.success(f"Worker registered!\nBlockchain Hash: {hash_val}\nPredicted Health Risk: {risk}")

# ---------------- Doctor Dashboard ----------------
elif role == "Doctor":
    st.header("👩‍⚕ Doctor Dashboard")
    if st.session_state.workers:
        df = pd.DataFrame(st.session_state.workers)
        st.dataframe(df)
        st.info("You can view worker records here.")
    else:
        st.warning("No worker records available.")

# ---------------- Government Analytics ----------------
else:
    st.header("📊 Government Analytics")
    total = len(st.session_state.workers)
    st.metric("Total Workers Registered", total)
    if total > 0:
        df = pd.DataFrame(st.session_state.workers)
        st.subheader("Age Distribution")
        st.bar_chart(df["Age"])
