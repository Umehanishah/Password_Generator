import streamlit as st
import random
import string

def generate_password(name, extra_chars, level):
    if level == "Weak":
        length = 8
        chars = string.ascii_letters
    elif level == "Medium":
        length = 12
        chars = string.ascii_letters + string.digits
    else:  # Strong
        length = 16
        chars = string.ascii_letters + string.digits + string.punctuation
    
    total_length = len(name) + len(extra_chars)
    if total_length >= length:
        return name + extra_chars  # If input is too long, return as is
    
    random_chars = ''.join(random.choices(chars, k=length - total_length))
    password = name + extra_chars + random_chars
    password = ''.join(random.sample(password, len(password)))  # Shuffle password for randomness
    return password

# Page Config
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #FFEBEB;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with Custom Styling
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🔐 Secure Password Generator</h1>
    <h3 style='text-align: center;'>Create a strong, unique password instantly!</h3>
""", unsafe_allow_html=True)

# Input Fields
name = st.text_input("Enter a name or keyword:")
extra_chars = st.text_input("Enter numbers or symbols:")
level = st.slider("Select password strength:", 1, 3, 2, format=None)

# Convert slider value to text
level_map = {1: "Weak", 2: "Medium", 3: "Strong"}
level_text = level_map[level]

# Generate Password Button
if st.button("Generate Password"):
    if not name.strip() or not extra_chars.strip():
        st.warning("⚠️ Please enter both name and extra characters!")
    else:
        password = generate_password(name.strip(), extra_chars.strip(), level_text)
        st.success(f"✅ Your Generated Password: `{password}`")

# Footer with Custom Styling
st.markdown("""
    <hr>
    <p style='text-align: center;'>🔒 Keep your password secure and unique! | <b>Created by Hanishah</b></p>
""", unsafe_allow_html=True)
