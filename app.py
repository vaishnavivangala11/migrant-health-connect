import streamlit as st
import pandas as pd
from datetime import datetime
import hashlib
import random

st.set_page_config(page_title="Migrant Health Connect", page_icon="💊")

# In-memory "database"
if "workers" not in st.session_state:
    st.session_state.workers = []

st.title("💊 Migrant Health Connect – Prototype")

# Sidebar menu for roles
role = st.sidebar.radio("Login as", ["Worker", "Doctor", "Government"])

# ---------------- Worker Registration ----------------
if role == "Worker":
    st.header("👷 Worker Registration")
    st.info("Problem in Kerala: Migrant workers often move frequently and lose their past health records. They face repeated tests, language barriers, and difficulty communicating with doctors in new locations.")
    
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    language = st.selectbox("Preferred Language", ["English", "Malayalam","Hindi","Bengali","Odia","Tamil","Assamese","Telugu"])
    
    # Upload medical report
    report = st.file_uploader("Upload your latest medical report (PDF/Images)", type=["pdf","png","jpg","jpeg"])
    
    if st.button("Register"):
        # Save record
        record = {
            "Name": name, 
            "Age": age, 
            "Gender": gender,
            "Language": language,
            "Report": report.name if report else "No report uploaded",
            "Date": datetime.now()
        }
        st.session_state.workers.append(record)

        # Blockchain hash demo
        hash_val = hashlib.sha256(f"{name}{age}{datetime.now()}".encode()).hexdigest()

        # AI demo (predictive health risk)
        risk = random.choice(["Low", "Medium", "High"])

        st.success(f"✅ Worker registered!")
        st.info(f"Blockchain Hash: {hash_val}")
        st.info(f"Predicted Health Risk: {risk}")

# ---------------- Doctor Dashboard ----------------
elif role == "Doctor":
    st.header("👩‍⚕ Doctor Dashboard")
    st.info("Doctors can view migrant workers’ past records and uploaded reports.")
    
    if st.session_state.workers:
        df = pd.DataFrame(st.session_state.workers)
        st.dataframe(df)

        # Show uploaded reports
        st.subheader("Uploaded Reports")
        for w in st.session_state.workers:
            if w.get("Report") and w["Report"] != "No report uploaded":
                st.write(f"{w['Name']}'s report: {w['Report']}")
    else:
        st.warning("No worker records available.")

# ---------------- Government Analytics ----------------
else:
    st.header("📊 Government Analytics")
    st.info("Government can see total registered workers and age distribution to plan healthcare schemes.")
    
    total = len(st.session_state.workers)
    st.metric("Total Workers Registered", total)
    
    if total > 0:
        df = pd.DataFrame(st.session_state.workers)
        st.subheader("Age Distribution")
        st.bar_chart(df["Age"])
