from dotenv import load_dotenv
load_dotenv()  # loading all the env variables
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# config your Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def get_response(prompt, image, input):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def get_image_details(uploaded_file):
    # read the file in bytes
    bytes_data = upload_file.getvalue()

    image_parts = [
        {
            'mime_type' : uploaded_file.type,
            'data' : bytes_data
        }
    ]
    return image_parts

# initialize streamlit app
st.set_page_config(page_title="Invoice Extractor", page_icon="🤖")

st.header("MultiLanguage Invoice Extractor")

input = st.text_input("Input Prompt: ", key="input")

upload_file = st.file_uploader("Choose a Invoice", type=["jpg", "jpeg", "png"])
img = ""
if upload_file is not None:
    image = Image.open(upload_file)  # Open the image file
    st.image(image, caption="File uploaded!", use_column_width=True)

# submit button
submit = st.button("Ask something about the invoice")

# input prompt
input_prompt = """
You are an expert in uderstanding invoices. We will upload a image as invoice
and you will have to answer any questions based on the uploaded invoice image
"""

# if user clicked submit
if submit:
    image_data = get_image_details(upload_file)
    response = get_response(input_prompt, image_data, input)
    st.subheader("Bot:")
    st.write(response)