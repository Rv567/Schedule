import streamlit as st
import threading
import schedule
import time
from datetime import datetime

# Shared state to trigger updates
if 'message' not in st.session_state:
    st.session_state.message = ""

# Function to update shared state
def my_scheduled_function():
    st.session_state.message = f"Function ran at: {datetime.now()}"

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

# Display the latest message
st.write(st.session_state.message)
