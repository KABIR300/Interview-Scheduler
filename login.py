import streamlit as st
from hr_interface import authenticate

def login():
    """
    Function to handle user login.

    Returns:
    bool: True if login is successful, False otherwise.
    """
    st.subheader('Login')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        if authenticate(email, password):
            st.success('Login successful!')
            return True
        else:
            st.error('Invalid email or password. Please try again.')
            return False
