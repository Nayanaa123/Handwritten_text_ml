import streamlit as st
import pandas as pd
from PIL import Image
import io
import random

st.set_page_config(
    page_title="Handwritten Text Generator",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_parquet("datasets/train-00000-of-00001.parquet")

df = load_data()

st.markdown("""
<style>
.stApp{
background:#f8fafc;
}
.main-container{
max-width:1000px;
margin:auto;
padding-top:40px;
}
.title{
font-size:42px;
font-weight:700;
color:#0f172a;
text-align:center;
margin-bottom:8px;
}
.subtitle{
font-size:17px;
color:#64748b;
text-align:center;
margin-bottom:35px;
}
textarea{
border-radius:12px !important;
}
div.stButton > button{
width:100%;
background:#2563eb;
color:white;
border:none;
padding:14px;
font-size:17px;
font-weight:600;
border-radius:12px;
}
.footer{
text-align:center;
margin-top:40px;
font-size:14px;
color:#94a3b8;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Handwritten Text Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Convert typed text into handwritten output using dataset samples</div>', unsafe_allow_html=True)

text = st.text_area(
    "Enter your text",
    height=180,
    placeholder="Type your sentence here..."
)

def crop_word_from_line(img, line_text, word):
    if word not in line_text:
        return None

    width = img.width
    height = img.height

    start = line_text.find(word)
    end = start + len(word)

    char_width = width / max(len(line_text), 1)

    left = int(start * char_width)
    right = int(end * char_width)

    return img.crop((left, 0, right, height))

def get_word_image(word):
    matches = df[df["text"].str.lower().str.contains(word.lower(), na=False)]

    if len(matches) == 0:
        return None

    sample = matches.sample(1).iloc[0]

    line_text = str(sample["text"]).lower()

    img_bytes = sample["image"]["bytes"]
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")

    return crop_word_from_line(img, line_text, word.lower())

if st.button("Generate Handwriting"):
    if text.strip():
        words = text.split()
        word_images = []

        for word in words:
            img = get_word_image(word)
            if img:
                word_images.append(img)

        if word_images:
            total_width = sum(img.width for img in word_images) + 20 * len(word_images)
            max_height = max(img.height for img in word_images)

            final_img = Image.new(
                "RGB",
                (total_width + 40, max_height + 40),
                "white"
            )

            x = 20
            for img in word_images:
                final_img.paste(img, (x, 20))
                x += img.width + 20

            st.image(
                final_img,
                use_container_width=True
            )
        else:
            st.error("No matching handwritten words found")

st.markdown(
    '<div class="footer">Developed by Nayana</div>',
    unsafe_allow_html=True
)