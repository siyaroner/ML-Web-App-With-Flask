import numpy as np
from flask import Flask, render_template,request

# from joblib import load

app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def hello_world():
    request_type_str=request.method
    if request_type_str == 'GET':
        return render_template("index.html")
    # else:
    #     text=request.form["text"]
    #     return text.upper()