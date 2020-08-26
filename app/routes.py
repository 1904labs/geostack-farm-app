import os
import json
from flask import current_app as app
from flask import render_template, send_from_directory
from app.manifests import CraManifest

@app.context_processor
def manifest_processor():
    return {"manifest": CraManifest()}

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
