import streamlit as st

st.title("Settings")

st.header('Default selections')

st.selectbox("Dealer group", ["Group 1", "Group 2", "Group 3"], key="default_sel_dealer_group")
if st.session_state.sel_dealer_group:
    st.multiselect('Locations',["Site 1","Site 2","Site 3","Site 4"], key="default_sel_dealer_site")