from flask import Flask, redirect, url_for, request, render_template
import base64
import numpy as np
from keras.models import load_model
# pip install scipy==1.1.0
from scipy.misc import imsave, imread, imresize
import re
import sys 
import os

app = Flask(__name__)


prediction = ''



def convertImage(imgData1):
	imgstr = re.search(r'base64,(.*)',imgData1).group(1)
	#print(imgstr)
	with open('output.png','wb') as output:
		output.write(imgstr.decode('base64'))

@app.route('/')
def home():
	return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
	if request.method == 'POST':
		imgData = request.get_data()
		convertImage(imgData)
		x = imread('output.png',mode='L')
		x = np.invert(x)
		x = imresize(x,(34,34))
		x = x.reshape(1,34,34,3)
		__MODEL = "model/model_alphabets.h5"
		model = load_model(__MODEL)
		result = model.predict(x)
		global prediction
		prediction = str(np.argmax(result[0]))
		print(result, prediction)
		return redirect('/')


if __name__ == "__main__":
	app.run()