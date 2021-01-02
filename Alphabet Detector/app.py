from flask import Flask, redirect, url_for, request, render_template
import io
from PIL import Image
import base64
import numpy as np
from keras.models import load_model
import cv2

app = Flask(__name__)


__MODEL = "model/alphabets_model.h5"
model = load_model(__MODEL)

@app.route('/')
def home():
	return render_template("app.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
	if request.method == 'POST':
		file = request.get_json()
		image = file['image']
		__image = image[image.find('/9'):]
		img = Image.open(io.BytesIO(base64.b64decode(__image)))
		img = img.resize((224, 224), Image.ANTIALIAS)
		img = np.array(img)
		image = np.expand_dims(img, axis = 0)
		result = model.predict(image)
		if int(round(result[0][0])) == 1:
		  print("A")
		if int(round(result[0][1])) == 1:
		  print("B")
		if int(round(result[0][2])) == 1:
		  print("C")
		if int(round(result[0][3])) == 1:
		  print("D")
		if int(round(result[0][4])) == 1:
		  print("E")
		if int(round(result[0][5])) == 1:
		  print("F")
		if int(round(result[0][6])) == 1:
		  print("G")
		if int(round(result[0][7])) == 1:
		  print("H")
		if int(round(result[0][8])) == 1:
		  print("I")
		if int(round(result[0][9])) == 1:
		  print("J")
		if int(round(result[0][10])) == 1:
		  print("K")
		if int(round(result[0][11])) == 1:
		  print("L")
		if int(round(result[0][12])) == 1:
		  print("M")
		if int(round(result[0][13])) == 1:
		  print("N")
		if int(round(result[0][14])) == 1:
		  print("O")
		if int(round(result[0][15])) == 1:
		  print("P")
		if int(round(result[0][16])) == 1:
		  print("Q")
		if int(round(result[0][17])) == 1:
		  print("R")
		if int(round(result[0][18])) == 1:
		  print("S")
		if int(round(result[0][19])) == 1:
		  print("T")
		if int(round(result[0][20])) == 1:
		  print("U")
		if int(round(result[0][21])) == 1:
		  print("V")
		if int(round(result[0][22])) == 1:
		  print("X")
		if int(round(result[0][23])) == 1:
		  print("Y")
		if int(round(result[0][24])) == 1:
		  print("Z")
		return redirect('/')


if __name__ == "__main__":
	app.run(debug=True)