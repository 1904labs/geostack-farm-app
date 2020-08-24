import os
from flask import current_app as app
from flask import render_template, send_from_directory

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/manifest.json')
def manifest():
    return send_from_directory('dist', 'manifest.json')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('dist', 'favicon.ico')

@app.route('/logo192.png')
def logo192():
    return send_from_directory('dist', 'logo192.png')

@app.route('/logo512.png')
def logo512():
    return send_from_directory('dist', 'logo512.png')