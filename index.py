# # from flask import Flask, request
# # import streamlit as st
# # import threading

# # app = Flask(__name__)

# # @app.route('/getdata/<url>', methods=['POST'])
# # def get_data(url):
# #     print('URL::::', url)
# #     # Implement your logic to return data
# #     # For example, fetching some data and returning it as JSON
# #     data = {"key": "value"}  # Replace with your data fetching logic
# #     st.write('API hits')
# #     return data

# # def run_flask():
# #     app.run(port=5000)  # Run on a different port than Streamlit

# # # Run Flask in a separate thread
# # threading.Thread(target=run_flask).start()

# # # Streamlit app code here
# # st.title('My Streamlit App')
# # # ...


# from flask import Flask, request, jsonify
# import threading

# app = Flask(__name__)

# @app.route('/api/getdata', methods=['GET'])
# def get_data():
#     # Your logic to fetch and return data
#     data = {"message": "Hello from Streamlit + Flask!"}
#     return jsonify(data)

# @app.route('/api/postdata', methods=['POST'])
# def post_data():
#     # Example of handling POST data
#     received_data = request.json
#     return jsonify({"received": received_data})

# def run_flask():
#     app.run(port=5000)

# # Run Flask in a separate thread
# threading.Thread(target=run_flask).start()


import streamlit as st
import pandas as pd

# Create a DataFrame with some data
data = {'Name': ['John', 'Jane', 'Bob'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Create a Streamlit app that returns the data as JSON
@st.cache
def get_data():
    return df.to_json()

@st.route('/data')
def data():
    return get_data()

if __name__ == '__main__':
    st.run_app()

