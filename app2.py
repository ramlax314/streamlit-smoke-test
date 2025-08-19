import streamlit as st
import sys, platform, os

st.set_page_config(page_title="Streamlit Smoke Test", page_icon="✅", layout="centered")

st.title("✅ Streamlit Cloud Smoke Test")
st.write("If you can see this, your deployment pipeline works.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Environment")
    st.code(f"Python: {sys.version.split()[0]}\nPlatform: {platform.platform()}")
with col2:
    st.subheader("Working dir")
    st.code(os.getcwd())

st.subheader("Interactive check")
name = st.text_input("Your name", "Runner")
st.write(f"Hello, {name} 👋")

st.subheader("Simple chart (no extra packages)")
values = [1, 3, 2, 5, 4, 6]
st.line_chart(values)

st.caption("Tip: If this deploys but your main app fails, simplify requirements.txt and add missing packages one by one.")
