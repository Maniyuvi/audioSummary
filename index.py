from flask import Flask, request
import streamlit as st
import threading

app = Flask(__name__)

@app.route('/getdata/<url>', methods=['POST'])
def get_data(url):
    print('URL::::', url)
    # Implement your logic to return data
    # For example, fetching some data and returning it as JSON
    data = {"key": "value"}  # Replace with your data fetching logic
    return data

def run_flask():
    app.run(port=3000)  # Run on a different port than Streamlit

# Run Flask in a separate thread
threading.Thread(target=run_flask).start()

# Streamlit app code here
st.title('My Streamlit App')
# ...
