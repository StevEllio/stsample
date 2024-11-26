import streamlit as st
import numpy as np

st.header("Request 1")
st.write(f"You are logged in as {st.session_state.role}.")




tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

with tab1:
    st.subheader("A tab with a chart")
    st.line_chart(data)

with tab2:
    st.subheader("A tab with the data")
    st.write(data)