import streamlit as st


st.header("Respond 1")
st.write(f"You are logged in as {st.session_state.role}.")


st.write('Dealer group selected: ' + st.session_state.sel_dealer_group)