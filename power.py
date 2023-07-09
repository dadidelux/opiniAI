import streamlit as st
import openai
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()


# Function to communicate with ChatGPT
def chat_with_gpt(prompt):
    configure()
    #openai.api_key = st.secrets["api_key"]
    openai.api_key = os.getenv("api_key")
    response = openai.Completion.create(
        engine="text-babbage-001",
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

# Streamlit app
st.markdown(
    """
    <style>
    body {
        background-color: #e6e6fa;
        color: #000000; /* Updated font color to black */
        font-family: 'Georgia', serif;
    }
    p {
        color: #000000;
    }
    h2 {
        color: #000000;
    }

    h1 {
        color: #800000;
        font-family: 'Raleway', sans-serif;
        margin-bottom: 20px;
    }

    input,
    select {
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    button {
        background-color: #483d8b;
        color: #FFFFFF; /* Updated font color to black */
        border: none;
        border-radius: 4px;
        font-family: 'Raleway', sans-serif;
        padding: 8px 16px;
        text-decoration: none;
        cursor: pointer;
    }
    
    button p {
        color:#ffffff;
    }

    button:hover {
        background-color: #e64a19;
    }

    .widget-box {
        background-color: #000000;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 16px;
        padding: 30px;
    }

    .reportview-container {
        background: #fff8e1;
    }

    .main {
        background: #fff8e1;
    }

    .block-container {
        background: #fff8e1;
    }
    </style>

    """,
    unsafe_allow_html=True,
)

st.title("Ask Any Hobby Toys Description")

# Choose input type
with st.sidebar:
    st.header("Instructions")
    st.write("Introducing Ask Any Hobby Toys Description Maker - your go-to app for generating concise and accurate descriptions of hobby toys. Simply input the toy details, and instantly receive a polished, 50-word description. Save time, enhance your product listings, and captivate customers with this essential tool for hobbyists and toy sellers.")
    input_type = st.selectbox("Choose input type:", ["SKU", "Product Name"])

# Get user input
if input_type == "SKU":
    SKU = st.text_input("Enter the Traxxas SKU:")
    prompt = f"Can you provide me with product description for the Traxxas SKU {SKU}? "
else:   
    product_name = st.text_input("Enter the Traxas Product name:")
    prompt = f"Can you provide me with product description for the Traxxas product name {product_name}? "

chat_response = ""

# Send query to the chatbot
if st.button("Search for it!"):
    chat_response = chat_with_gpt(prompt)
    
    # Split the response into lines and find the recipe name
    lines = chat_response.split('\n')
    product_name = ""
    steps = ""
    for line in lines:
        if "Traxxas product name" in line.lower():
            chat_name = line.strip()
        else:
            steps += line.strip() + "\n"

    # Output
    with st.container():
        st.markdown(f"## {product_name}")
        st.markdown(steps)

# Share on WhatsApp
import urllib

# Inside the if condition
if st.button("Share on WhatsApp"):
    share_text = f"Check out this product descriptor bot that you can play with: {chat_response}"
    share_text = urllib.parse.quote(share_text)
    st.markdown(f"<a href='https://api.whatsapp.com/send?text={share_text}' target='_blank'>Share on WhatsApp</a>", unsafe_allow_html=True)