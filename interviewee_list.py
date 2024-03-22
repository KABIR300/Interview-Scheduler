import streamlit as st
import pandas as pd
from hr_interface import get_interviewees
from datetime import datetime, timedelta

INTERVIEW_DURATION = timedelta(minutes=30)
INTERVIEW_START_TIME = datetime.strptime('11:00', '%H:%M')
INTERVIEW_END_TIME = datetime.strptime('23:59', '%H:%M')
WAITING_TIME = timedelta(hours=24)



def interviewee_list_component():
    """
    Component to display the list of interviewees in a table with remaining time slots.
    """
    st.subheader('HR Interface')
    interviewees = get_interviewees()
    if interviewees:
        interviewee_data = {'ID': [], 'Name': [], 'Email': [], 'Waiting Time': []}
        for interviewee in interviewees:
            interviewee_data['ID'].append(interviewee['id'])
            interviewee_data['Name'].append(interviewee['name'])
            interviewee_data['Email'].append(interviewee['email'])
            interviewee_data['Waiting Time'].append(calculate_remaining_time(interviewee))

        st.write(pd.DataFrame(interviewee_data))
    else:
        st.write('No interviewees registered yet.')

    

        
def calculate_remaining_time(interviewee):
    """
    Calculate the remaining time slots based on interviewee's availability.
    """
    current_time = datetime.now()

    total_time_slots = (INTERVIEW_END_TIME - INTERVIEW_START_TIME) // INTERVIEW_DURATION

    if interviewee.get('Availability'):
        for slot in interviewee['Availability']:
            start_time, end_time = map(lambda x: datetime.strptime(x, '%H:%M'), slot.split('-'))
            if current_time < end_time:  # Check if the current time is before the end time of the slot
                remaining_slots = (end_time - current_time) // INTERVIEW_DURATION
                remaining_hours, remaining_minutes = divmod(remaining_slots.total_seconds() // 3600, 60)
                remaining_time = f"{remaining_hours} hours and {remaining_minutes} minutes"
                return remaining_time

    return "Not Available"


