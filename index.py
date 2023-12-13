import streamlit as st
from flask import Flask, request, jsonify
 
# Initialize Flask app
app = Flask(__name__)
 
# Streamlit UI
st.title('Streamlit App with API Endpoint')
 
# Endpoint to receive Salesforce requests
@app.route('/receive-from-salesforce', methods=['POST'])
def receive_from_salesforce():
    print('receive_from_salesforce')
    # Get data from Salesforce request
    request_data = request.json
 
    # Process data received from Salesforce
    # Perform necessary actions based on the data
 
    # Return response to Salesforce
    response_data = {'message': 'Received data successfully'}
    return jsonify(response_data)
 
# Run the Streamlit app with Flask
if __name__ == '__main__':
    app.run(port=8501)


# # # from flask import Flask, request
# # # import streamlit as st
# # # import threading

# # # app = Flask(__name__)

# # # @app.route('/getdata/<url>', methods=['POST'])
# # # def get_data(url):
# # #     print('URL::::', url)
# # #     # Implement your logic to return data
# # #     # For example, fetching some data and returning it as JSON
# # #     data = {"key": "value"}  # Replace with your data fetching logic
# # #     st.write('API hits')
# # #     return data

# # # def run_flask():
# # #     app.run(port=5000)  # Run on a different port than Streamlit

# # # # Run Flask in a separate thread
# # # threading.Thread(target=run_flask).start()

# # # # Streamlit app code here
# # # st.title('My Streamlit App')
# # # # ...


# # from flask import Flask, request, jsonify
# # import threading

# # app = Flask(__name__)

# # @app.route('/api/getdata', methods=['GET'])
# # def get_data():
# #     # Your logic to fetch and return data
# #     data = {"message": "Hello from Streamlit + Flask!"}
# #     return jsonify(data)

# # @app.route('/api/postdata', methods=['POST'])
# # def post_data():
# #     # Example of handling POST data
# #     received_data = request.json
# #     return jsonify({"received": received_data})

# # def run_flask():
# #     app.run(port=5000)

# # # Run Flask in a separate thread
# # threading.Thread(target=run_flask).start()


# # import streamlit as st
# # import pandas as pd

# # # Create a DataFrame with some data
# # data = {'Name': ['John', 'Jane', 'Bob'], 'Age': [25, 30, 35]}
# # df = pd.DataFrame(data)

# # # Create a Streamlit app that returns the data as JSON
# # @st.cache
# # def get_data():
# #     return df.to_json()

# # @st.route('/data')
# # def data():
# #     return get_data()

# # if __name__ == '__main__':
# #     st.run_app()

# # import streamlit as st
# # import extra_streamlit_components as stx

# # @st.cache_resource(hash_funcs={"_thread.RLock": lambda _: None})
# # def init_router():
# #     return stx.Router({"/home": home, "/landing": landing})

# # def home():
# #     return st.write("This is a home page")

# # def landing():
# #     return st.write("This is the landing page")

# # router = init_router()
# # router.show_route_view()

# # c1, c2, c3 = st.columns(3)

# # with c1:
# #     st.header("Current route")
# #     current_route = router.get_url_route()
# #     st.write(f"{current_route}")
# # with c2:
# #     st.header("Set route")
# #     new_route = st.text_input("route")
# #     if st.button("Route now!"):
# #         router.route(new_route)
# # with c3:
# #     st.header("Session state")
# #     st.write(st.session_state)


# # from flask import Flask, render_template
# # import streamlit as st

# # app = Flask(__name__)
# # @app.route('/')
# # def index():
# #     st.write("Test")
# #     return {"Test" : "Test"}
# # @app.route('/url')
# # def url():
# #     st.set_page_config(page_title="My Streamlit App")
# #     st.write("Hello, world!")
# #     return {"Dome" : "ss"}
# # if __name__ == '__main__':
# #     app.run()

# import streamlit as st
 
# if not hasattr(st, 'already_started_server'):
#     # Hack the fact that Python modules (like st) only load once to
#     # keep track of whether this file already ran.
#     st.already_started_server = True
 
#     st.write('''
#         The first time this script executes it will run forever because it's
#         running a Flask server.
 
#         Just close this browser tab and open a new one to see your Streamlit
#         app.
#     ''')
 
#     from flask import Flask
 
#     app = Flask(__name__)
 
#     @app.route('/foo')
#     def serve_foo():
#         return 'This page is served via Flask!'
 
#     app.run(port=8888)
 
 
# # We'll never reach this part of the code the first time this file executes!
 
# # Your normal Streamlit app goes here:
# x = st.slider('Pick a number')
# st.write('You picked:', x)

