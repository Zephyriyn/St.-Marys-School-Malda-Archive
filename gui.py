import streamlit as st
import pandas as pd
import sqlite3
from PIL import Image
import os
import inspect
st.set_page_config(
    page_title="St. Mary's, Malda",
    layout="wide",
    initial_sidebar_state="expanded",
)

current_directory = os.getcwd()
def show_google_map_from_query(query):
    url = f"https://www.google.com/maps/search/{query}/"
    return url
def display_students_list(data):
    st.dataframe(data.style.highlight_max(axis=0))
def get(name):
    options = [{"Admission No":"admission_no"},
            {"Previous School":"prevschool"},
            {"Date of Birth":"dateofbirth"},
            {"Father's Name":"fathername"},
            {"Mobile Noy":"mobile_no"},
            {"Email ID":"emailid"},
            {"Current Address:":"current"},
            {"Name":"student_name"}]
    for option in options:
        for key, value in option.items():
            if key == name:
                print("hi")
                print(value)
                return value
def display_student_details(data):
    
    st.title(f"{data['student_name']}")
    current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    img =  Image.open(current_directory + "/Master_Img/" + data['pfp'])
    
    with st.expander("Picture"):
        st.image(img,caption=data['student_name'],use_column_width='auto')
    

    st.subheader('Personal Information')
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Admission No: :blue[{data['admission_no']}]")
        st.write(f"Admission Date: :blue[{data['admission_date']}]")
        st.write(f"Session: :blue[{data['session']}]")
        st.write(f"Class: :blue[{data['class']}]")
        st.write(f"Section: :blue[{data['section']}]")
        st.write(f"Roll No: :blue[{data['rollno']}]")
        st.write(f"House: :blue[{data['house']}]")
        st.write(f"Date of Birth: :blue[{data['dateofbirth']}]")
        st.write(f"Place of Birth: :blue[{data['placeof_birth']}]")
        st.write(f"Certificate No: :blue[{data['certificate_no']}]")
        st.write(f"Blood Group: :blue[{data['bloodgroup']}]")
        st.write(f"Aadhar No: :blue[{data['aadharno']}]")
        st.write(f"Gender: :blue[{data['gender']}]")
        st.write(f"Religion: :blue[{data['religion']}]")
        st.write(f"Ration Type: :blue[{data['ration_type']}]")
        st.write(f"Category: :blue[{data['category']}]")
        st.write(f"Certificate: :blue[{data['certificate']}]")
        st.write(f"Mother Tongue: :blue[{data['mother_tongue']}]")
        st.write(f"Any Illness: :blue[{data['anyillness']}]")
        st.write(f"Previous School: :blue[{data['prevschool']}]")
        st.write(f"Cast: :blue[{data['cast']}]")
    with col2:
        st.write(f"Father's Name: :blue[{data['fathername']}]")
        st.write(f"Occupation (Father): :blue[{data['occupation']}]")
        st.write(f"Qualification (Father): :blue[{data['qualification']}]")
        st.write(f"Nationality: :blue[{data['nationality']}]")
        st.write(f"Marital Status: :blue[{data['maritalstatus']}]")
        st.write(f"Mobile No: :blue[{data['mobile_no']}]")
        st.write(f"Email ID: :blue[{data['emailid']}]")
        st.write(f"Guardian Name: :blue[{data['guardianname']}]")
        st.write(f"Parent Income: :blue[{data['parent_income']}]")
        st.write(f"Mother's Name: :blue[{data['mother']}]")
        st.write(f"Occupation (Mother): :blue[{data['occupation_mother']}]")
        st.write(f"Mother's Qualification: :blue[{data['mother_qualification']}]")
        st.write(f"Mother's Mobile No: :blue[{data['mobileno_mother']}]")
        st.write(f"Email Code: :blue[{data['emailcode']}]")
    st.divider()  
    st.subheader('Address Details')
    col3, col4 = st.columns(2)
    with col3:
        st.write(f"Current Address: :blue[{data['current']}]")
        st.write(f"Mobile No (Current): :blue[{data['mobile_no_current']}]")
        st.write(f"City/Village (Current): :blue[{data['cityvillage_current']}]")
        st.write(f"District (Current): :blue[{data['district_current']}]")
        st.write(f"Post Office (Current): :blue[{data['po_current']}]")
        st.write(f"Police Station (Current): :blue[{data['ps_current']}]")
        st.write(f"State (Current): :blue[{data['state_current']}]")
        st.write(f"Pincode: :blue[{data['pincode']}]")
    with col4:
        st.write(f"Permanent Address: :blue[{data['permanent_address']}]")
        st.write(f"Mobile No (Permanent): :blue[{data['mobile_no_permanent']}]")
        st.write(f"City/Village (Permanent): :blue[{data['cityvillage_permanent']}]")
        st.write(f"District (Permanent): :blue[{data['district_permanent']}]")
        st.write(f"Post Office (Permanent): :blue[{data['po_permanent']}]")
        st.write(f"Police Station (Permanent): :blue[{data['ps_permanent']}]")
        st.write(f"State (Permanent): :blue[{data['state_permanent']}]")
        st.write(f"Pincode (Permanent): :blue[{data['pincode_permanent']}]")
        st.write(f"Account Holder Name: :blue[{data['account_holder_name']}]")
        st.write(f"Account Name: :blue[{data['account_name']}]")
        st.write(f"IFSC Code: :blue[{data['IFSCCode']}]")
        st.write(f"Bank Name: :blue[{data['bankname']}]")
        st.write(f"Branch Name: :blue[{data['branch_name']}]")
    st.divider()
    st.subheader('Maps')
    col5, col6 = st.columns(2)
    with col5:
        ln1 = show_google_map_from_query(data['cityvillage_current'])
        html = f"""
<div style="width: 100%;"><iframe width="100%" height="600" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=en&amp;q={data['cityvillage_current']}()&amp;t=&amp;z=17&amp;ie=UTF8&amp;iwloc=B&amp;output=embed"><a href="https://www.maps.ie/population/">Population Estimator map</a></iframe></div>"""
        st.components.v1.html(f'<a href="{ln1}" target="_blank">View Current Address on Google Maps</a>', 150, 150)
    with col6:
        ln2 = show_google_map_from_query(data['cityvillage_permanent'])
        st.components.v1.html(f'<a href="{ln2}" target="_blank">View Permanent Address on Google Maps</a>', 150, 150)

    st.components.v1.html(html, height=600, width=730)
    st.divider()
# Connect to SQLite database
conn = sqlite3.connect('School Records V_0.2 - mine.sqbpro')

# Load data from the table
df = pd.read_sql_query("SELECT * from DATA_STUDENTS", conn)

conn.close()

# Create a Streamlit app
st.title("St. Mary's Malda")
mode = st.sidebar.radio("Mode", ("Search", "List"))
# Search functionality
if mode == "Search":
    col1, col2 = st.columns(2)
    search_term = col1.text_input('Search:')
    options = ["Name","Admission No",
"Previous School",
"Date of Birth",
"Father's Name",
"Mobile No",
"Email ID",
"Current Address",]
    
    search_column = col2.selectbox(label="Search By:", options=options,help="Select an option")
        
    if search_term:
        filteblue_df = df[df[f'{get(search_column)}'].astype(str).str.contains(search_term, case=False)]
        if filteblue_df.empty:
            st.warning('No results found')
        else:
            st.divider()
            st.write('Search Results:')
            st.write(filteblue_df)
            st.divider()

    # Display student details when a row is clicked
    if "filteblue_df" in globals():
        if not filteblue_df.empty:
            selected_index = st.selectbox('Select a student:', filteblue_df.index)
            selected_student = filteblue_df.loc[selected_index]
            display_student_details(selected_student)

elif mode == "List":
    st.write("List mode selected.")
    display_students_list(df)
