import streamlit as st


st.header("Request 2")
st.write(f"You are logged in as {st.session_state.user_role}.")


st.write('Dealer group selected: ' + st.session_state.st_sel_dealer_group)
