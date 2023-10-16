import streamlit as st
import pandas as pd
import sqlite3
import folium
from PIL import Image
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import requests, os
import inspect
current_directory = os.getcwd()
def show_google_map_from_query(query):
    url = f"https://www.google.com/maps/place/{query}/@25.0184128,88.1422793,17z/data=!4m6!3m5!1s0x39fafdbc15fd5ad3:0x78f588b004c7cf59!8m2!3d25.0180425!4d88.1456078!16s%2Fg%2F1td6dw_k?entry=ttu"
    return url
def display_students_list(data):
    st.dataframe(data.style.highlight_max(axis=0))
def display_student_details(data):
    st.title(f"Student Details - {data['student_name']}")
    current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    img =  Image.open(current_directory + "/Master_Img/" + data['pfp'])
    with st.expander("Picture"):
        st.image(img,caption=data['student_name'],use_column_width='auto')
    

    st.subheader('Personal Information')
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"Admission No: {data['admission_no']}")
        st.write(f"Admission Date: {data['admission_date']}")
        st.write(f"Session: {data['session']}")
        st.write(f"Class: {data['class']}")
        st.write(f"Section: {data['section']}")
        st.write(f"Roll No: {data['rollno']}")
        st.write(f"House: {data['house']}")
        st.write(f"Date of Birth: {data['dateofbirth']}")
        st.write(f"Place of Birth: {data['placeof_birth']}")
        st.write(f"Certificate No: {data['certificate_no']}")
        st.write(f"Blood Group: {data['bloodgroup']}")
        st.write(f"Aadhar No: {data['aadharno']}")
        st.write(f"Gender: {data['gender']}")
        st.write(f"Religion: {data['religion']}")
        st.write(f"Ration Type: {data['ration_type']}")
        st.write(f"Category: {data['category']}")
        st.write(f"Certificate: {data['certificate']}")
        st.write(f"Mother Tongue: {data['mother_tongue']}")
        st.write(f"Any Illness: {data['anyillness']}")
        st.write(f"Previous School: {data['prevschool']}")
        st.write(f"Cast: {data['cast']}")
    with col2:
        st.write(f"Father's Name: {data['fathername']}")
        st.write(f"Occupation (Father): {data['occupation']}")
        st.write(f"Qualification (Father): {data['qualification']}")
        st.write(f"Nationality: {data['nationality']}")
        st.write(f"Marital Status: {data['maritalstatus']}")
        st.write(f"Mobile No: {data['mobile_no']}")
        st.write(f"Email ID: {data['emailid']}")
        st.write(f"Guardian Name: {data['guardianname']}")
        st.write(f"Parent Income: {data['parent_income']}")
        st.write(f"Mother's Name: {data['mother']}")
        st.write(f"Occupation (Mother): {data['occupation_mother']}")
        st.write(f"Mother's Qualification: {data['mother_qualification']}")
        st.write(f"Mother's Mobile No: {data['mobileno_mother']}")
        st.write(f"Email Code: {data['emailcode']}")

    st.subheader('Address Details')
    col3, col4 = st.columns(2)
    with col3:
        st.write(f"Current Address: {data['current']}")
        st.write(f"Mobile No (Current): {data['mobile_no_current']}")
        st.write(f"City/Village (Current): {data['cityvillage_current']}")
        st.write(f"District (Current): {data['district_current']}")
        st.write(f"Post Office (Current): {data['po_current']}")
        st.write(f"Police Station (Current): {data['ps_current']}")
        st.write(f"State (Current): {data['state_current']}")
        st.write(f"Pincode: {data['pincode']}")
    with col4:
        st.write(f"Permanent Address: {data['permanent_address']}")
        st.write(f"Mobile No (Permanent): {data['mobile_no_permanent']}")
        st.write(f"City/Village (Permanent): {data['cityvillage_permanent']}")
        st.write(f"District (Permanent): {data['district_permanent']}")
        st.write(f"Post Office (Permanent): {data['po_permanent']}")
        st.write(f"Police Station (Permanent): {data['ps_permanent']}")
        st.write(f"State (Permanent): {data['state_permanent']}")
        st.write(f"Pincode (Permanent): {data['pincode_permanent']}")
        st.write(f"Account Holder Name: {data['account_holder_name']}")
        st.write(f"Account Name: {data['account_name']}")
        st.write(f"IFSC Code: {data['IFSCCode']}")
        st.write(f"Bank Name: {data['bankname']}")
        st.write(f"Branch Name: {data['branch_name']}")

    st.subheader('Maps')
    col5, col6 = st.columns(2)
    with col5:
        ln1 = show_google_map_from_query(data['cityvillage_current'])
        st.components.v1.html(f'<a href="{ln1}" target="_blank">View Current Address on Google Maps</a>', 150, 150)

    with col6:
        ln2 = show_google_map_from_query(data['cityvillage_permanent'])
        st.components.v1.html(f'<a href="{ln2}" target="_blank">View Permanent Address on Google Maps</a>', 150, 150)
# Connect to SQLite database
conn = sqlite3.connect('School Records.db')

# Load data from the table
df = pd.read_sql_query("SELECT * from DATA_STUDENTS", conn)

# Close the connection
conn.close()

# Create a Streamlit app
st.title('Student Database Search')
mode = st.sidebar.radio("Mode", ("Search", "List"))
# Search functionality
if mode == "Search":
    search_term = st.text_input('Enter student name to search:')

    # Filter data based on search term
    if search_term:
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        if filtered_df.empty:
            st.warning('No results found')
        else:
            st.write('Search Results:')
            st.write(filtered_df)

    # Display student details when a row is clicked
    if "filtered_df" in globals():
        if not filtered_df.empty:
            selected_index = st.selectbox('Select a student:', filtered_df.index)
            selected_student = filtered_df.loc[selected_index]
            display_student_details(selected_student)
elif mode == "List":
    st.write("List mode selected.")
    display_students_list(df)