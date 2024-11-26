import streamlit as st
import datetime


st.set_page_config(page_title='My app', page_icon=":material/thumb_up:", layout="wide")
st.info('This is a purely informational message', icon="ℹ️")

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Requester", "Responder", "Admin"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()

def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("pages/settings.py", title="Settings", icon=":material/settings:")

request_1 = st.Page("pages/request/request_1.py", title="Request 1", icon=":material/help:", default=(role == "Requester"))
request_2 = st.Page("pages/request/request_2.py", title="Request 2", icon=":material/bug_report:")
respond_1 = st.Page("pages/respond/respond_1.py", title="Respond 1", icon=":material/healing:", default=(role == "Responder"))
respond_2 = st.Page("pages/respond/respond_2.py", title="Respond 2", icon=":material/handyman:")
admin_1 = st.Page("pages/admin/admin_1.py", title="Admin 1", icon=":material/person_add:", default=(role == "Admin"))
admin_2 = st.Page("pages/admin/admin_2.py", title="Admin 2", icon=":material/security:")

st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.role in ["Requester", "Admin"]:
    page_dict["Request"] = [request_1, request_2]
if st.session_state.role in ["Responder", "Admin"]:
    page_dict["Respond"] = [respond_1, respond_2]
if st.session_state.role == "Admin":
    page_dict["Admin"] = [admin_1, admin_2]




# Widgets shared by all the pages





if len(page_dict) > 0:
    with st.sidebar:
        st.title('Filters')
        st.subheader('Group structure')
        st.selectbox("Dealer group", ["Group 1", "Group 2", "Group 3"], key="sel_dealer_group")
        st.multiselect('Locations',["Site 1","Site 2","Site 3","Site 4"], key="sel_dealer_site")
        
       
        st.subheader('Date')
        st.date_input("Date range",[datetime.date.today(),datetime.date.today()])
    pg = st.navigation(page_dict | {"Account": [settings,logout_page]})
else:
    pg = st.navigation([st.Page(login)])



pg.run()
