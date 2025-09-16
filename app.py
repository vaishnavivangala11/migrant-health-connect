import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Migrant Health Connect", page_icon="💊")

# Simple in-memory “database”
if "workers" not in st.session_state:
    st.session_state.workers = []

st.title("💊 Migrant Health Connect")

menu = st.sidebar.radio("Menu", ["Register Worker", "Doctor View", "Analytics"])

if menu == "Register Worker":
    st.header("👷 Worker Registration")
    name = st.text_input("Name")
    age = st.number_input("Age", 1, 100)
    gender = st.selectbox("Gender", ["Male","Female","Other"])
    phone = st.text_input("Phone Number")
    if st.button("Save Record"):
        st.session_state.workers.append({
            "Name": name, "Age": age, "Gender": gender,
            "Phone": phone, "Date": datetime.now()
        })
        st.success("✅ Worker record saved!")

elif menu == "Doctor View":
    st.header("👩‍⚕ Doctor Dashboard")
    if st.session_state.workers:
        df = pd.DataFrame(st.session_state.workers)
        st.dataframe(df)
        st.info("Doctor can view/update records here.")
    else:
        st.warning("No records yet.")

else:
    st.header("📊 Government Analytics")
    st.write("Total Workers Registered:", len(st.session_state.workers))
    if st.session_state.workers:
        df = pd.DataFrame(st.session_state.workers)
        st.bar_chart(df["Age"])
