import streamlit as st

st.title("Demo")

for i in range(10):
    st.text(f"Rango de 0 a 9: {i}")

for i in range(10, 26):
    st.text(f"rango de 10 a 25: {i}")

for i in range(10, 30, 2):
    st.text(f"rango de 10 a 30 en segmentos de 2: {i}")
