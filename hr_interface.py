import streamlit as st
import pandas as pd
from interviewee import get_interviewees

def hr_interface():
    """
    Function to display HR Interface.
    """
    st.subheader('HR Interface')
    interviewees = get_interviewees()
    if interviewees:
        interviewee_data = {'ID': [], 'Name': [], 'Email': [], 'Availability': []}
        for interviewee in interviewees:
            interviewee_data['ID'].append(interviewee['id'])
            interviewee_data['Name'].append(interviewee['name'])
            interviewee_data['Email'].append(interviewee['email'])
            interviewee_data['Availability'].append(interviewee['availability'])
        
        st.write(pd.DataFrame(interviewee_data))
    else:
        st.write('No interviewees registered yet.')


def authenticate(email: str, password: str) -> bool:
    """
    Authenticate HR personnel based on email and password.

    Args:
    email (str): Email of the HR personnel.
    password (str): Password of the HR personnel.

    Returns:
    bool: True if authentication is successful, False otherwise.
    """
    authorized_users = {
        'hr1@example.com': 'password1',
        'hr2@example.com': 'password2'
    }
    if email in authorized_users and authorized_users[email] == password:
        return True
    return False
