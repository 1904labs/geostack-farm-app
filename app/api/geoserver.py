import os
import requests
from . import api_bp
from flask import jsonify, request

geoserver = os.environ.get('GEOSERVER_URL', "http://localhost:8081")

@api_bp.route('/ext', methods=['GET'])
def get_ext():
    '''
    example: http%3A%2F%2F127.0.0.1%3A8081%2Fgeoserver%2Ftopp%2Fows%3Fservice%3DWFS%26version%3D1.0.0%26request%3DGetFeature%26typeName%3Dtopp%3Astates%26maxFeatures%3D50%26outputFormat%3Dapplication%2Fjson
    '''
    url = request.args.get('url')
    response = requests.get(url)
    return response.text

@api_bp.route('/geoserver', methods=['GET'])
def get():
    return jsonify({"geoserver": geoserver})

@api_bp.route('/geoserver/states', methods=['GET'])
def get_states():
    endpt = geoserver + '/geoserver/topp/ows'
    params = {
        "service": "WFS",
        "version": "1.0.0",
        "request": "GetFeature",
        "typeName": "topp:states",
        "maxFeatures": "50",
        "outputFormat": "application/json"
        }
    response = requests.get(endpt, params=params)
    return response.text
