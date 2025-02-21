import streamlit as st

# Custom CSS for background and animation
st.markdown("""
    <style>
    body {
        background-color: #ffe6e6;
    }
    .header {
        font-size: 40px;
        color: #ff3366;
        text-align: center;
        font-weight: bold;
        animation: pulse 2s infinite;
    }
    .subheader {
        font-size: 26px;
        color: #660033;
        font-style: italic;
    }
    .apology-text {
        font-size: 20px;
        color: #333333;
        padding: 15px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 2px 2px 10px #999;
        margin: 20px 0;
        text-align: justify;
    }
    .animated-heart {
        font-size: 50px;
        color: #ff3366;
        animation: beat 1.5s infinite;
        text-align: center;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    @keyframes beat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
    </style>
""", unsafe_allow_html=True)

# Title and Header
st.markdown('<div class="header">I’m Sorry 💔</div>', unsafe_allow_html=True)

# Animated Heart Icon
st.markdown('<div class="animated-heart">❤️</div>', unsafe_allow_html=True)

# Heartfelt Hinglish Apology
apology_text = """
Mujhe pata hai maine tumhe hurt kiya, aur is baat ka mujhe bohot afsos hai.  
Main kabhi bhi aise kuch nahi karna chahta tha jo tumhe dukh de.  
Please ek baar aur maaf kar do aur hamesha ki tarah smile kar do. 😔💖  
Tum meri duniya ho, aur tumhare bina sab adhoora lagta hai. 🌟
"""
st.markdown(f'<div class="apology-text">{apology_text}</div>', unsafe_allow_html=True)

# Display an online image of flowers
flower_image_url = "https://www.publicdomainpictures.net/pictures/320000/velka/beautiful-flower-bouquet.jpg"
st.image(flower_image_url, caption="Sending virtual flowers 🌸")

# Button to reveal a special message
if st.button("Click here for a special message 💌"):
    st.markdown('<div class="subheader">Mujhse naraz mat raho. Tum meri sabse pyaari ho. ❤️</div>', unsafe_allow_html=True)

# Contact button for opening communication
st.write("Jab bhi ready ho, please baat kar lena.")
if st.button("Message me 💬"):
    st.write("Tumhare bina sab kuch incomplete lagta hai. 🙏")
