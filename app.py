# importing the required libraries
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import mne
import os
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt

# initialising the flask app
app = Flask(__name__)

# The path for uploading the file
@app.route('/')
def upload_file():
   return render_template('upload.html')

@app.route('/edf/upload', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST': # check if the method is post
      f = request.files['file'] # get the file from the files object
      print(f);
      f.save(secure_filename(f.filename)) # this will secure the file
      EEG = mne.io.read_raw_edf(f.filename)
      rs = EEG.plot()
      rs.savefig('outFig.jpg')
      # f = open('outFig.jpg', "rb")
      #  return render_template('image_render.html', image=file)
      return send_file('outFig.jpg', mimetype='image/jpg', as_attachment="true")
      # return 'file uploaded successfully' # Display thsi message after uploading
		

@app.route('/set/download', methods = ['GET', 'POST'])
def setDownload():                
    # os.remove(f.filename);
      fd=send_file('outFig.jpg', mimetype='image/jpg', as_attachment="true")
      print("fd >>>>>>", fd)
      return fd          

if __name__ == '__main__':
   app.run() # running the flask app