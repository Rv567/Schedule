import streamlit as st
import threading
import schedule
import time
from datetime import datetime

# Your function to be scheduled
def my_scheduled_function():
    st.write(f"Function is running: {datetime.now()}")
    # Add your function logic here

# Function to run the scheduler
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Schedule your function to run every day at a specific time
schedule.every().day.at("08:00").do(my_scheduled_function)

# Start the scheduler in a separate thread if not already started
if 'scheduler_thread' not in st.session_state:
    st.session_state.scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    st.session_state.scheduler_thread.start()

# Streamlit app code
st.title("My Streamlit App with Scheduler")
st.write("The function will run every day at 08:00 AM")

# Additional app content
st.write("This is the main content of the app.")
