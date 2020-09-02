import os
import json
import requests
from app.api import api_bp
from flask import jsonify, request, abort, current_app
from .logger import logger
from .gs import Geoserver


# define geoserver api
gs_url = os.environ.get('GEOSERVER_URL', "http://localhost:8081")
gs_username = os.environ.get('GEOSERVER_ADMIN_USER', "admin")
gs_password = os.environ.get('GEOSERVER_ADMIN_PASSWORD', "geoserver")
geoserver_api = Geoserver(gs_url, gs_username, gs_password)

# define geoserver workspaces api
gs_workspace = os.environ.get('GEOSERVER_WORKSPACE', "default")
workspace_api = geoserver_api.workspace(gs_workspace)

# define geoserver workspaces datastore api
pg_database = os.environ.get('POSTGRES_DB', "gis")
pg_host = os.environ.get('POSTGRES_HOST', "localhost")
pg_port = os.environ.get('POSTGRES_PORT', 5432)
pg_user = os.environ.get('POSTGRES_USER', "gis")
pg_pwd = os.environ.get('POSTGRES_PASS', "postgres")
datastore_api = workspace_api.pg_datastore(pg_database, pg_host, pg_port, pg_user, pg_pwd)


@api_bp.route('/ext', methods=['GET'])
def get_ext():
    url = request.args.get('url')
    response = requests.get(url)
    return response.text


@api_bp.route('/ext/example', methods=['GET'])
def get_ext_example():
    return jsonify({"example": u"http%3A%2F%2F127.0.0.1%3A8081%2Fgeoserver%2Ftopp%2Fows%3Fservice%3DWFS%26version%3D1.0.0%26request%3DGetFeature%26typeName%3Dtopp%3Astates%26maxFeatures%3D50%26outputFormat%3Dapplication%2Fjson"})


@api_bp.route('/geoserver', methods=['GET'])
def get():
    global gs_url
    return jsonify({"geoserver": gs_url})


@api_bp.route('/geoserver/states', methods=['GET'])
def get_states():
    endpt = gs_url + '/topp/ows'
    params = {
        "service": "WFS",
        "version": "1.0.0",
        "request": "GetFeature",
        "typeName": "topp:states",
        "maxFeatures": "50",
        "outputFormat": "application/json"
    }
    response = requests.get(endpt, params=params)
    return response.json()


@api_bp.route(
    f'/geoserver/rest/workspaces/{gs_workspace}/datastores/{pg_database}', methods=['GET'])
@api_bp.route(f'/geoserver/rest/workspaces/{gs_workspace}/datastores/{pg_database}/<path:path>', methods=['GET'])
def get_datastore_proxy(path: str = '') -> str:
    try:
        return datastore_api.get(path).json()
    except json.JSONDecodeError:
        return abort(400)


@api_bp.route(f'/geoserver/rest/workspaces/{gs_workspace}', methods=['GET'])
@api_bp.route(f'/geoserver/rest/workspaces/{gs_workspace}/<path:path>', methods=['GET'])
def get_workspace_proxy(path: str = '') -> str:
    try:
        return workspace_api.get(path).json()
    except json.JSONDecodeError:
        return abort(400)


@api_bp.route('/geoserver/rest', methods=['GET'])
@api_bp.route('/geoserver/rest/<path:path>', methods=['GET'])
def get_geoserver_proxy(path: str = '') -> str:
    try:
        return geoserver_api.get(path).json()
    except json.JSONDecodeError:
        return abort(400)
