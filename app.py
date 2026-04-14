from flask import Flask,request,jsonify
import sqlite3
from flask_cors import CORS
import pandas as pd
import os
from flask import render_template

app=Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def home():
    return "API is working"

@app.route('/games',methods=['GET'])
def all():
    c=sqlite3.connect('test.db')
    cur=c.cursor()
    cur.execute("SELECT * FROM games")
    data=cur.fetchall()
    cur.close()
    return jsonify(data)
@app.route('/games/<category>',methods=['GET'])
def category(category):
    c=sqlite3.connect('test.db')
    cur=c.cursor()
    cur.execute("SELECT * FROM games WHERE gametype=?", (category,))
    data=cur.fetchall()
    cur.close()
    return jsonify(data)
if __name__=='__main__':
    app.run(debug=os.getenv('FLASK_DEBUG','False')=='True')