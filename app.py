import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai

st.title("Smart Document AI")
st.write("Upload a PDF document to extract structured data.")

#1. Authenticate with Google safely using the hidden secret key

try:
  genai.configure(api_key = st.secrets["GEMINI_API_KEY"])
  model = genai.GenerativeModel('gemini-3.1-flash')
except KeyError:
  st.error("API Key not found. Please ensure GEMINI_API_KEY is set in Streamlit Secrets.")
  st.stop()

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
  with st.expander("Click to view raw text"):
    st.text_area(label = "Parsed contents", value = extracted_text, height = 200)

  st.subheader("AI Analysis")

  if st.button("Extract Data with AI"):
    with st.spinner("Analyzing document with Gemini..."):
      prompt = f"""
      You are an expert data extraction assistant.
      Review the following document text and extract the key information.

      Return the data as a clean JSON object.
      Do not include markdown formatting in the output, just the raw JSON.

      Please extract:
      - Document Title
      - Main Subject or Purpose
      - Key Dates or Financial Years mentioned
      - A brief 2-sentence summary of the document 

      Document Text:
      {extracted_text}
      """

      try:
        response = model.generate_content(prompt)

        st.success("Extraction Complete!")
        st.json(response.text)

      except Exception as e:
        st.error(f"An error occurred during AI processing: {e}")
