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
    
    random_chars = ''.join(random.choices(chars, k=length - len(name + extra_chars)))
    password = name + extra_chars + random_chars
    password = ''.join(random.sample(password, len(password)))  # Shuffle password for randomness
    return password

# Page Config
st.set_page_config(page_title="Password Generator", page_icon="🔑", layout="centered")

# Title with Custom Styling
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🔐 Secure Password Generator</h1>
    <h3 style='text-align: center;'>Create a strong, unique password instantly!</h3>
""", unsafe_allow_html=True)

# Sidebar for Inputs
with st.sidebar:
    st.header("🔧 Customize Your Password")
    name = st.text_input("Enter a name or keyword:")
    extra_chars = st.text_input("Enter numbers or symbols:")
    level = st.selectbox("Select password strength:", ["Weak", "Medium", "Strong"])
    generate_btn = st.button("Generate Password")

# Main Content with Columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if generate_btn:
        if not name or not extra_chars:
            st.warning("⚠️ Please enter both name and extra characters!")
        else:
            password = generate_password(name, extra_chars, level)
            st.success(f"✅ Your Generated Password: `{password}`")

# Footer with Custom Styling
st.markdown("""
    <hr>
    <p style='text-align: center;'>🔒 Keep your password secure and unique! | <b>Made with ❤️ using Streamlit</b></p>
""", unsafe_allow_html=True)
