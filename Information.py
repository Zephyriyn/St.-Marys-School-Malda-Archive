
import streamlit as st
from utils import *

st.set_page_config("Information Panel", page_icon="data/icon.png")
st.write("Authored by Zephyriyn.")

csvPath="data/2023-24.csv"
information = [{'Admission Date': '15/03/2023', 'Admission No': '2391', 'Session': '2023-2024', 'Class': 'CLASS VIII', 'Section': 'A', 'Roll Number': '17.0', 'First Sem': '0', "Student's Name": 'AYUSHI SINGHA', 'Gender': 'Female', 'Date Of Birth': '28-07-2010', "Father's Name": 'SUMAN SINGHA', "Father's Qualification": '', "Mother's Name": 'RUMPA S SINGHA', "Mother's Qualification": '', 'Identifacation Mark': '&nbsp;', 'Current School': '&nbsp;', "Guardian's Name": 'SUMAN SINGHA', 'Relation': 'Not Available', 'Occupation': 'Central Govt. Job', 'Religion': 'Hindu', 'Cast': 'Select', "Parent's Income": '&nbsp;', 'Under The Care of': 'SUMAN SINGHA', 'City': 'LAKE GARDEN, GHORAPIR, MALDA', 'Post Office': 'MALDA', 'Police Station': 'MALDA', 'District': 'MALDA', 'Pin': '732101', 'Mobile No.': '9680634461', 'Under The Care of Permanent': 'SUMAN SINGHA', 'Permanent City': 'LAKE GARDEN, GHORAPIR, MALDA', 'Permanent Post Office': 'MALDA', 'Permanent Police Station': 'MALDA', 'Permanent District': 'MALDA', 'Pincode': '732101', 'Paymenet Status': 'Paid', 'Hostel Taken': 'No', 'Transportation Taken': 'No', 'Transfer Status': 'NT', 'Bus No.': '', 'Aadhar No.': '&nbsp;', 'RTE': 'Select', 'House/Group': 'BOSCO', 'Previous Roll No.': '', 'Previous Section': '', 'Roll Used': '', 'Staff Ward': 'Select', 'Mobile 2': '8209788171', 'Email Id': '&nbsp;', 'Birth Certificate No': '&nbsp;', 'Place of Birth': '&nbsp;', 'Blood Group': 'A+', 'Cast Certificate No.': '&nbsp;', "Student's Mother Tounge": 'Hindi', 'Has Illness?': 'NO', "Father's Nationality": 'INDIAN', "Father's Marital Status": 'Married', "Mother's Marital Status": 'Married', "Mother's Nationality": 'INDIAN', "Mother's Occupation": 'House Wife', 'Ration Type': 'APL', 'Illness Remark': '&nbsp;', "Father's Mobile No.": '9680634461', "Mother's Email": '', 'Account Holder Name': '&nbsp;', 'Bank Name': '&nbsp;', 'IFSC Code': '&nbsp;', 'Branch Name': '&nbsp;', 'Admission Type': 'Old Admission', 'Status': 'Active', 'Password': '123', 'pfp': 'https://smsmalda.com/Master_Img/Student/StudentImg20220819010546.jpeg'}]
Options = getCSVHeaders(csvPath=csvPath)
Options = ["All"] + Options

def OnSearch():
    keyword = Search
    results = []
    
    if (Header == "All" and Class == "All"):
        results = searchByAll(csvPath=csvPath, keyword=keyword)
    elif (Header == "All" and Class != "All"):
        results = searchByAllAndClass(csvPath=csvPath, keyword=Search, Class=Class)
    elif (Header != "All"):
        if (Class != "All"):
            results = searchByMultipleHeaders(csvPath=csvPath, headerKeywordPairs={"Class": Class, Header: Search})
        else:
            results = searchByHeader(csvPath=csvPath, header=Header, keyword=Search)

    if (results != [] and results != None):
        for result in results:
            st.write(result)
    else:
        st.write("No Results Found😔")

left, right = st.columns(2)

Search = left.text_input("Search", "", help="Enter the keyword.")
Header = right.selectbox("By", options=Options, help="Select header to search by.")
Class = right.selectbox("Class", options=["All"] + getPossibleHeaderValues(csvPath=csvPath, header="Class"))

if Search:
    OnSearch()
