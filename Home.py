import streamlit as st
import pickle
import streamlit_authenticator as stauth
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Vodafone Customer Churn Prediction",
    page_icon="🚪",
    layout='wide'
)

# --- USER AUTHENTICATION ---
names = ['Visitor', 'Admin']
usernames = ['user', 'admin']

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
if not file_path.exists():
    st.error("Error: hashed_pw.pkl file not found. Please generate it.")
else:
    with file_path.open("rb") as file:
        hashed_passwords = pickle.load(file)

    authenticator = stauth.Authenticate(
        names, usernames, hashed_passwords, 'churn_app', 'abcdefg', cookie_expiry_days=30
    )

    # --- LANDING PAGE ---
    col1, col2 = st.columns(2)

    with col2:
        name, authentication_status, username = authenticator.login('Login', 'main')
        st.session_state['name'] = name
        st.session_state['authentication_status'] = authentication_status
        st.session_state['username'] = username

        if authentication_status is None:
            st.info('Please log in to continue')
            st.markdown('### **Demo credentials**')
            st.write('Username: user')
            st.write('Password: abc123')

    with col1:
        if authentication_status is None:
            st.title('Welcome to the Vodafone Customer Churn Prediction App')
            st.write('''
                An end to end machine learning project developed by [Laaria_Chris](https://github.com/laaria-chris/Vodafone-Customer-Churn-Project).
            ''')

    # Handle failed login
    if authentication_status is False:
        st.error("Invalid username or password. Please try again.")
        st.markdown('### **Demo credentials**')
        st.write('Username: user')
        st.write('Password: abc123')

    # Main app content
    if authentication_status:
        st.success(f"Welcome, {name}! You are logged in.")
        st.title("Customer Churn Prediction App")
        st.write("""
        Use this application to analyze and predict customer churn using advanced machine learning techniques.
        """)
        authenticator.logout("Logout", "main")
