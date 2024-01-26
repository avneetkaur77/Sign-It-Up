import pickle
from flask import Flask, requests, jsonify, render_template, url_for
from camera import VideoCamera
# import requests
import base64,cv2
app = Flask(__name__)
model = pickle.load(open('model.p', 'rb'))

@app.route('/')
def home():
    # Run your Python code here
    # result = my_python_function()  # Replace with your function or code

    # return f'The result is: {result}'
    return render_template('signitup.html')

@app.route('/vcplt')
def vcplt():
    return render_template('vcplt.html')




if __name__ == '__main__':
    app.run(debug=True)
#     import os

# Get the absolute file path of the model.pkl file
# model_file_path = os.path.join(os.path.dirname(__file__), 'path', 'to', 'model.pkl')

# # Load the pickled model
# with open(model_file_path, 'rb') as f:
#     model = pickle.load(f)

