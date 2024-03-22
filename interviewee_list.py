import streamlit as st
import pandas as pd
from hr_interface import get_interviewees
from datetime import datetime, timedelta

INTERVIEW_DURATION = timedelta(minutes=30)
INTERVIEW_START_TIME = datetime.strptime('11:00', '%H:%M')
INTERVIEW_END_TIME = datetime.strptime('23:30', '%H:%M')
WAITING_TIME = timedelta(hours=24)



def interviewee_list_component():
    """
    Component to display the list of interviewees in a table with remaining time slots.
    """
    st.title('Interviewee List')

    # Get interviewees data
    interviewees = get_interviewees()

    if interviewees:
        # Create a DataFrame from the interviewees data
        df = pd.DataFrame(interviewees, columns=['Name', 'Email'])

        # Calculate remaining time for each interviewee
        df['Remaining Time'] = df.apply(calculate_remaining_time, axis=1)

        # Display the DataFrame as a table without row and column index
        st.write(pd.DataFrame(df))
        st.write(datetime.now())
    else:
        st.write("No interviewees registered yet.")

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
                remaining_hours, remaining_minutes = divmod((remaining_slots.seconds // 3600), 60)
                remaining_time = f"{remaining_hours} hours and {remaining_minutes} minutes"
                return remaining_time

    remaining_hours, remaining_minutes = divmod((total_time_slots * INTERVIEW_DURATION).seconds // 3600, 60)
    remaining_time = f"{remaining_hours} hours and {remaining_minutes} minutes"
    return remaining_time
