import streamlit as st

st.title("Smart Document AI")
st.write("Upload a PDF document to extract structured data.")

#uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type = ["pdf"])

if uploaded_file is not None:
  st.success(f"Successfully uploaded: {uploaded_file.name}")
  file_details = {
    "Filename": uploaded_file.name,
    "Filetype": uploaded_file.type,
    "FileSize (bytes)": uploaded_file.size
  }
  st.write(file_details)
