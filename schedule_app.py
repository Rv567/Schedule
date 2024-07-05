import streamlit as st
import schedule
import time
from datetime import datetime
import threading

# Streamlit app code
st.title("My Streamlit App with Scheduler")
st.write("The function will run every day at 08:00 AM")

# Your function to be scheduled
def my_scheduled_function():
    st.write(f"Function is running: {datetime.now()}")
    # Add your function logic here

schedule.every().day.at("08:00").do(my_scheduled_function)

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

# Function to run the scheduler
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

run_scheduler()
