import streamlit as st
from file_management import load_interviewees, save_interviewees

def register_interviewee():
    """
    Function to register interviewees.
    """
    st.subheader('Register Interviewee')
    name = st.text_input('Name')
    email = st.text_input('Email')
    if st.button('Register'):
        interviewees = load_interviewees()
        if any(interviewee['email'] == email for interviewee in interviewees):
            st.error('Already registered with this email.')
        else:
            interviewee_id = len(interviewees) + 1
            interviewee = {'id': interviewee_id, 'name': name, 'email': email, 'availability': ''}
            interviewees.append(interviewee)
            save_interviewees(interviewees)
            st.success('Registration Successful!')


def get_interviewees():
    """
    Function to retrieve all interviewees.
    """
    interviewees = load_interviewees()
    return interviewees
