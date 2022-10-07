from flask import Flask, render_template
import cv2
from PIL import Image, ImageTk
import tkinter as tk
import cv2
import os
import numpy as np
import tensorflow as tf
import keras
import operator
import time
import sys
import matplotlib.pyplot as plt
import os
from string import ascii_uppercase
port = 5100

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/template')
def application():
	f = open(r'C:/Users/prane/OneDrive/Desktop/EDT/app.py','r').read()
	return exec(f)
	
@app.route('/')
def login():
	return render_template('login.html')

@app.errorhandler(404)
def TypeError():
	return "TypeError"

if __name__=="__main__":
	app.run(host="0.0.0.0",port=port,debug=True)