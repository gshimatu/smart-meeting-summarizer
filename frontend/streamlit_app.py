import streamlit as st

st.set_page_config(page_title="SmartMeeting Summarizer")

st.title("SmartMeeting Summarizer")

uploaded_file = st.file_uploader(
    "Upload meeting audio or text",
    type=["mp3", "wav", "txt"]
)

if uploaded_file:
    st.success("File ready for analysis (backend coming next)")
