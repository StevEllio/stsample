import streamlit as st
import datetime

# add role parameter and set to none
if "role" not in st.session_state:
    st.session_state.role = None
        
# set pages to wide
st.set_page_config(page_title='My app', page_icon=":material/thumb_up:", layout="wide")

hide_header = """
        [data-testid="stHeader"] {
            display: none;
        }
        """

hide_sidebar_toggle = """
        [data-testid="stSidebarCollapseButton"] {
            display: none;
        }        
        """
adjust_padding = """
        [data-testid="stMainBlockContainer"] {
            padding-left: 2rem;
            padding-right: 2rem;
            padding-top: 0rem;
        }
    """
    
# hide streamlit toolbars
hide_stuff = """<style>""" + hide_header + hide_sidebar_toggle + adjust_padding + """</style>"""
st.markdown(hide_stuff, unsafe_allow_html=True)

# placeholder for info bar
#st.info('This is a purely informational message', icon="ℹ️")

role = st.session_state.role

logout_page = st.Page("pages/logout.py", title="Log out", icon=":material/logout:")
settings = st.Page("pages/settings.py", title="Settings", icon=":material/settings:")

request_1 = st.Page("pages/request/request_1.py", title="Request 1", icon=":material/help:", default=(role == "Requester"))
request_2 = st.Page("pages/request/request_2.py", title="Request 2", icon=":material/bug_report:")
respond_1 = st.Page("pages/respond/respond_1.py", title="Respond 1", icon=":material/healing:", default=(role == "Responder"))
respond_2 = st.Page("pages/respond/respond_2.py", title="Respond 2", icon=":material/handyman:")
admin_1 = st.Page("pages/admin/admin_1.py", title="Admin 1", icon=":material/person_add:", default=(role == "Admin"))
admin_2 = st.Page("pages/admin/admin_2.py", title="Admin 2", icon=":material/security:")

st.logo("images/horizontal_blue.png")

page_dict = {}
if st.session_state.role in ["Requester", "Admin"]:
    page_dict["Request"] = [request_1, request_2]
if st.session_state.role in ["Responder", "Admin"]:
    page_dict["Respond"] = [respond_1, respond_2]
if st.session_state.role == "Admin":
    page_dict["Admin"] = [admin_1, admin_2]




# set defaults
selected_start_date = datetime.date.today()
selected_end_date = datetime.date.today() 

if "sel_date_period" not in st.session_state:
    st.session_state.sel_date_period = None
    

#selected_start_date = utils.DatesFromPeriod.Today
#selected_end_date = utils.DatesFromPeriod.Today


#st.session_state.sel_date_period = None



if len(page_dict) > 0:
    with st.sidebar:
        st.title('Filters')
        st.subheader('Group structure')
        st.selectbox("Dealer group", ["Group 1", "Group 2", "Group 3"], key="sel_dealer_group")
        st.multiselect('Locations',["Site 1","Site 2","Site 3","Site 4"], key="sel_dealer_site")
        
       
        st.subheader('Date')
        #st.selectbox("Date period",utils.DatesFromPeriod().list(),key="sel_date_period",placeholder="This updates date range")
        #with st.empty():
            #st.date_input("Date range",[selected_start_date,selected_end_date])
        st.button("Apply filters")
    pg = st.navigation(page_dict | {"Account": [settings,logout_page]})
else:
    pg = st.navigation([st.Page("pages/login.py")])



pg.run()
