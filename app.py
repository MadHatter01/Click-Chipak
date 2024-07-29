import streamlit as st
from openai import OpenAI


from openai import OpenAI

client = OpenAI()

st.set_page_config(page_title="ClickChipak", page_icon=":pencil:")

st.title("Click Chipak")



st.markdown(
    """
    <style>
    body {
        background-color: #121212; 
    }
       .muted-text {
        color: #888888;  /* Choose a muted color */
    }
    .stButton>button {
        background-color: #b3004d; 
        color: #ffffff; 
        border: 2px solid #00ffcc; 
        border-radius: 5px; 
        font-weight: bold;
        transition: background-color 0.3s ease, color 0.3s ease; make 
    }
    .stButton>button:hover {
        background-color: #ff4d94; 
        color: #121212; 
        border: 2px solid #00ffcc;
    }
    .stTextInput>div>input {
        background-color: #1e1e1e; 
        color: #00ffcc; 
        border: 2px solid #d81b60;
        border-radius: 5px; 
    }
    .stTextArea>div>textarea {
        background-color: #1e1e1e; 
        color: #00ffcc;
        border: 2px solid #d81b60; 
        border-radius: 5px; 
    }
    .generated-text{
    color:#ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div class='muted-text'>
    <p>
        Let’s face it: <strong>Lorem Ipsum</strong> is so last decade! While it’s the go-to for placeholders, it’s about as exciting as waiting in line at a grocery store.
    </p>
    <p>
        That’s why <strong>ClikChipak</strong> is here to serve up random, interesting content. It adds a dash of humor and keeps users engaged, turning my mockups into delightful experiences.
    </p>
    <p>
        <strong>Who wouldn’t want a bit of fun in their designs?</strong>
    </p>
</div>
""", unsafe_allow_html=True)
st.sidebar.header("Input")

api_key = st.sidebar.text_input("OpenAI API Key", type="password")

website_type = st.sidebar.text_input("Type of Website", "clothing" )

num_paragraphs = st.sidebar.slider("Number of Paragraphs", 1, 10, 3)
num_words = st.sidebar.slider("Number of words per paragraph", 50,500,100)

tone = st.sidebar.selectbox("Tone", ["Formal", "Neutral", "Informal", "Exciting", "Educational", "Persuasive", "Humorous", "Professional"])


generate_button = st.sidebar.button("Generate Text")

generated_text = st.empty()

def generate_text( num_paragraphs, num_words, tone):
    
    prompt = f"Generate {num_paragraphs} paragraphs of {num_words} words each in a {tone} tone for a {website_type} default copy"

    response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    max_tokens= num_paragraphs*num_words,
    temperature=0.6,
    messages = [
            {"role": "system", "content": "You are an experienced copywriter specializing in creating engaging product copy and taglines. You are asked to create default text for a website"},
            {"role": "user", "content": prompt}
        ])
    return response.choices[0].message.content


if generate_button:
    
    text = generate_text(num_paragraphs, num_words, tone)
    paragraphs = text.split('\n')
    formatted_text = "".join(f'<p class="generated-text">{paragraph}</p>' for paragraph in paragraphs)
    st.subheader("Generated Text")
    st.markdown(formatted_text, unsafe_allow_html=True)
