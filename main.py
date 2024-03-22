import streamlit as st
from interviewee import register_interviewee
from hr_interface import hr_interface
from login import login
from interviewee_list import interviewee_list_component

def main():
    """
    Main function to run the Streamlit app.
    """
    st.title('Interview Scheduler')

    menu = ['Registration', 'HR Interface','Interviewee List']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Registration':
        register_interviewee()
    elif choice == 'HR Interface':
        login_successful=login()
        if login_successful:
            hr_interface()
    elif choice == 'Interviewee List':
        interviewee_list_component()

if __name__ == '__main__':
    main()
