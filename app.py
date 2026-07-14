import streamlit as st
from pypdf import PdfReader

st.title("Smart Document AI")
st.write("Upload a PDF document to extract structured data.")

#uploader widget
uploaded_file = st.file_uploader("Choose a PDF file", type = ["pdf"])

if uploaded_file is not None:
  st.success(f"Successfully uploaded: {uploaded_file.name}")

  with st.spinner("Extracting text from PDF..."):
    reader = PdfReader(uploaded_file)
    extracted_text = ""
    for page in reader.pages:
      text = page.extract_text()
      if text:
        extracted_text += text +"\n"

  st.subheader("Extracted Raw Text:")
  st.text_area(
    label = "Review the parsed contents below:",
    value = extracted_text,
    height = 300
  )
