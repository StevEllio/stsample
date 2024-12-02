import streamlit as st
import datetime

# Initialise session parameters if not set
if "user_role" not in st.session_state:
    st.session_state.user_role = None


# set pages to wide
st.set_page_config(page_title='My app', page_icon=":material/thumb_up:", layout="wide")

HIDE_HEADER = """
        [data-testid="stHeader"] {
            display: none;
        }
        """
HIDE_SIDEBAR_TOGGLE = """
        [data-testid="stSidebarCollapseButton"] {
            display: none;
        }        
        """
ADJUST_PADDING = """
        [data-testid="stMainBlockContainer"] {
            padding-left: 2rem;
            padding-right: 2rem;
            padding-top: 0rem;
        }
    """
# hide streamlit toolbars
HIDE_STUFF = """<style>""" + HIDE_HEADER + HIDE_SIDEBAR_TOGGLE + ADJUST_PADDING + """</style>"""
st.markdown(HIDE_STUFF, unsafe_allow_html=True)

# placeholder for info bar
#st.info('This is a purely informational message', icon="ℹ️")

# define page routes
PAGE_LOGIN = st.Page("pages/login.py")
PAGE_LOGOUT = st.Page("pages/logout.py", title="Log out", icon=":material/logout:")
PAGE_SETTINGS = st.Page("pages/settings.py", title="Settings", icon=":material/settings:")

PAGE_REQUEST_1 = st.Page("pages/request/request_1.py", title="Request 1", icon=":material/help:", default=(st.session_state.user_role == "Requester"))
PAGE_REQUEST_2 = st.Page("pages/request/request_2.py", title="Request 2", icon=":material/bug_report:")
PAGE_RESPOND_1 = st.Page("pages/respond/respond_1.py", title="Respond 1", icon=":material/healing:", default=(st.session_state.user_role == "Responder"))
PAGE_RESPOND_2 = st.Page("pages/respond/respond_2.py", title="Respond 2", icon=":material/handyman:")
PAGE_ADMIN_1 = st.Page("pages/admin/admin_1.py", title="Admin 1", icon=":material/person_add:", default=(st.session_state.user_role == "Admin"))
PAGE_ADMIN_2 = st.Page("pages/admin/admin_2.py", title="Admin 2", icon=":material/security:")

PAGE_DICT = {}
if st.session_state.user_role in ["Requester", "Admin"]:
    PAGE_DICT["Request"] = [PAGE_REQUEST_1, PAGE_REQUEST_2]
if st.session_state.user_role in ["Responder", "Admin"]:
    PAGE_DICT["Respond"] = [PAGE_RESPOND_1, PAGE_RESPOND_2]
if st.session_state.user_role == "Admin":
    PAGE_DICT["Admin"] = [PAGE_ADMIN_1, PAGE_ADMIN_2]

st.logo("images/horizontal_blue.png")


# GLOBAL VARIABLES

TODAY = datetime.date.today()
YESTERDAY = TODAY - datetime.timedelta(1)
START_OF_MONTH = TODAY.replace(day=1)
START_OF_YEAR = TODAY.replace(day=1,month=1)

DATE_PERIODS = {
    "Today":[TODAY,TODAY],
    "Yesterday":[YESTERDAY,YESTERDAY],
    "MTD":[START_OF_MONTH,TODAY],
    "MTYD":[START_OF_MONTH,YESTERDAY],
    "YTD":[START_OF_YEAR,TODAY],
    "YTYD":[START_OF_YEAR,YESTERDAY]
}

if "st_sel_dates" not in st.session_state:
    selected_start_date = START_OF_MONTH
    selected_end_date = TODAY
else:
    selected_start_date = None
    selected_end_date = None
 
    
if st.session_state.st_sel_date_period:
    selected_start_date = DATE_PERIODS[st.session_state.st_sel_date_period][0]
    selected_end_date = DATE_PERIODS[st.session_state.st_sel_date_period][1]
    st.session_state.st_sel_date_period = None
    


if len(PAGE_DICT) > 0:
    with st.sidebar:
        st.title('Filters')
        st.subheader('Group structure')
        st.selectbox("Dealer group", ["Group 1", "Group 2", "Group 3"], key="st_sel_dealer_group")
        st.multiselect('Locations',["Site 1","Site 2","Site 3","Site 4"], key="st_sel_dealer_site")
        
       
        st.subheader('Date')
        st.selectbox("Date period",list(DATE_PERIODS),key="st_sel_date_period",placeholder="This updates date range")
        with st.empty():
            st.date_input("Date range",[selected_start_date,selected_end_date],key="st_sel_dates")
        st.button("Apply filters")
    pg = st.navigation(PAGE_DICT | {"Account": [PAGE_SETTINGS,PAGE_LOGOUT]})
else:
    pg = st.navigation([PAGE_LOGIN])


pg.run()