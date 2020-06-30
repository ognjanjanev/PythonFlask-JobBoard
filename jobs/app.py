import sqlite3
from flask import Flask, g
from flask import render_template

PATH = "db/jobs.sqlite"

app = Flask(__name__)

def open_connection():
    return getattr(o, g)

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
