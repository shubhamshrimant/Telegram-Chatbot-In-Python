# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:49:06 2021

@author: shubh
"""

from flask import Flask,render_template,request
import ss2
app = Flask(__name__,template_folder='C:\\Users\\shubh\\chatbot\\templates')

@app.route('/',methods=['GET','POST'])
def hello():
    res=[]
    if request.method=='POST':
        inp=request.form.get("input_user")
        res=ss2.chatbot(inp)
    return render_template('w.html',results=res)


if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)