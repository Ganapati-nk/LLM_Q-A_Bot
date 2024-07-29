from dotenv import load_dotenv
load_dotenv()


import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro')

def get_response(question):
    response=model.generate_content(question)
    return response.text


st.set_page_config(page_title="AskME")
st.header('AskME Q&A Bot Using Gemini LLM')


input=st.text_input("Input : ",key='input')

submit=st.button("Generate Answer")


if submit:
    response=get_response(input)
    st.write(response)