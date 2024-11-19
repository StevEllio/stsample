import streamlit as st

st.header("Page 2")
st.write(f"You are logged in as {st.session_state.role}.")
