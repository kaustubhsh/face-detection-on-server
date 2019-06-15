from flask import Flask,send_file
from flask import request, jsonify
import base64
import os
import numpy as np
import cv2
from io import StringIO
from flask_cors import CORS
from flask_ngrok import run_with_ngrok
import shutil
count=0
main_source=0
app=Flask(__name__)
CORS(app)
dirpath=os.getcwd()
#run_with_ngrok(app)

@app.route("/", methods=['POST','GET'])
def index():
	if request.method == 'POST':
		data=request.stream.read()
		data=str(data).split(',')[1] #.encode()
		global count
		count+=1
		img = base64.b64decode(data)
		npimg = np.frombuffer(img, dtype=np.uint8)
		source = cv2.imdecode(npimg, 1)
		if count <4:
			return ""
		elif count==1:
			os.mkdir('/images')
		elif count==100:
			shutil.rmtree("/images")
			os.mkdir('/images')
		cv2.imwrite('/images/hello1'+str(count)+'.jpg', source)
		face_cascade = cv2.CascadeClassifier(dirpath+'/haarcascade_frontalface_default.xml')
		face_img = source.copy()
		face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2)
		for (x,y,w,h) in face_rects: 
        		cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10) 
		global main_source
		cv2.imwrite(dirpath+'/images/hello'+str(count)+'.jpg', face_img)
		try:
			with open(dirpath+'/images/hello'+str(count)+'.jpg', 'rb') as image_file:
				encoded_string = base64.b64encode(image_file.read())
			main_source=encoded_string
		
		except:
			try:
				with open(dirpath+'/images/hello1'+str(count-1)+'.jpg', 'rb') as image_file:
					encoded_string = base64.b64encode(image_file.read())
				main_source=encoded_string
			except:
				with open(dirpath+'/images/hello1'+str(count-2)+'.jpg', 'rb') as image_file:
					encoded_string = base64.b64encode(image_file.read())
				main_source=encoded_string
		return ""
	else:	
		if type(main_source)==int:
			return ""
		return main_source
if __name__ == "__main__":
	app.run()
