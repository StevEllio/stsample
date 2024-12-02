import streamlit as st


ROLES = [None, "Requester", "Responder", "Admin"]


col1, col2, col3 = st.columns(3)
with col2:
    st.container(height=200,border=False)
    row2 = st.container(border=True)
    with row2:
        st.header("Log in")
        st.text_input("Username")
        st.text_input("Password",type="password")
        user_role = st.selectbox("Choose your role", ROLES)
        if st.button("Log in"):
            st.session_state.user_role = user_role
            st.rerun()
