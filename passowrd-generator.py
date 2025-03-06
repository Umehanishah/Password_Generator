import streamlit as st
import random
import string

def generate_password(name, extra_chars, level):
    if level == "Weak":
        length = 6
        chars = string.ascii_letters
    elif level == "Medium":
        length = 8
        chars = string.ascii_letters + string.digits
    else:  # Strong
        length = 10
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

# Input Fields
name = st.text_input("✏️ Enter a name or keyword:")
extra_chars = st.text_input("🔢 Enter numbers or symbols:")

# Custom Slider for Password Strength
level = st.radio("⚡ Select Password Strength:", ["Weak 🟡", "Medium 🟠", "Strong 🔴"])

# Generate Password Button
if st.button("🔑 Generate Password"):
    if not name.strip() or not extra_chars.strip():
        st.warning("⚠️ Please enter both name and extra characters!")
    else:
        level_text = level.split()[0]  # Extract strength text (Weak, Medium, Strong)
        password = generate_password(name.strip(), extra_chars.strip(), level_text)
        st.success(f"✅ Your Generated Password: `{password}`")

# Footer with Custom Styling
st.markdown("""
    <hr>
    <p style='text-align: center'>🔒 Keep your password secure and unique! | <b>Created by Hanishah</b></p>
""", unsafe_allow_html=True)
