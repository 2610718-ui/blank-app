import streamlit as st

st.title("🔢 구구단 전체 출력")

for i in range(2, 10):
    st.subheader(f"--- {i}단 ---")
    for j in range(1, 10):
        st.text(f'{i} * {j} = {i*j}')