import streamlit as st
import numpy as np

st.header("Request 1")
st.write(f"You are logged in as {st.session_state.role}.")




tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)