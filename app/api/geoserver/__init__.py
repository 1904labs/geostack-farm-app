import json
import requests
from app.api import api_bp
from flask import jsonify, request, abort, current_app as app
from .gs import Geoserver
from werkzeug.local import LocalProxy

logger = LocalProxy(lambda: app.logger)

# define geoserver api
gs_url = app.config.get('GEOSERVER_URL', "http://127.0.0.1:8080")
gs_username = app.config.get('GEOSERVER_ADMIN_USER', "admin")
gs_password = app.config.get('GEOSERVER_ADMIN_PASSWORD', "geoserver")
geoserver_api = Geoserver(gs_url, gs_username, gs_password)

# define geoserver workspaces api
gs_workspace = app.config.get('GEOSERVER_WORKSPACE', "default")
workspace_api = geoserver_api.workspace(gs_workspace)

# define geoserver workspaces datastore api
pg_database = app.config.get('POSTGRES_DB', "gis")
pg_host = app.config.get('POSTGRES_HOST', "localhost")
pg_port = app.config.get('POSTGRES_PORT', 5432)
pg_user = app.config.get('POSTGRES_USER', "gis")
pg_pwd = app.config.get('POSTGRES_PASSWORD', "postgres")
datastore_api = workspace_api.pg_datastore(pg_database, pg_host, pg_port, pg_user, pg_pwd)

ft_name = 'points'
featuretype_api = datastore_api.featuretype(name=ft_name, data={
    "featureType": {
        "circularArcPresent": False,
        "enabled": True,
        "forcedDecimal": False,
        "maxFeatures": 0,
        "name": ft_name,
        "nativeName": ft_name,
        "numDecimals": 0,
        "overridingServiceSRS": False,
        "padWithZeros": False,
        "projectionPolicy": "FORCE_DECLARED",
        "serviceConfiguration": False,
        "skipNumberMatched": False,
        "srs": "EPSG:404000",
        "title": ft_name,
        "attributes": {
            "attribute": {
                "binding": "java.lang.String",
                "maxOccurs": 1,
                "minOccurs": 0,
                "name": "point",
                "nillable": True
            }
        },
        "keywords": {
            "string": [
                ft_name
            ]
        },
        "latLonBoundingBox": {
            "minx": -90,
            "maxx": 90,
            "miny": -180,
            "maxy": 180,
            "crs": "EPSG:4326"
        },
        "nativeBoundingBox": {
            "minx": -90,
            "maxx": 90,
            "miny": -180,
            "maxy": 180,
            "crs": "EPSG:4326"
        },
    }
})


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
    f'/geoserver/rest/workspaces/{gs_workspace}/datastores/{pg_database}/featuretypes/{ft_name}', methods=['GET'])
@api_bp.route(
    f'/geoserver/rest/workspaces/{gs_workspace}/datastores/{pg_database}/featuretypes/{ft_name}.json', methods=['GET'])
@api_bp.route(
    f'/geoserver/rest/workspaces/{gs_workspace}/datastores/{pg_database}/featuretypes/{ft_name}/<path:path>', methods=['GET'])
def get_featuretype_proxy(path: str = '') -> str:
    response = featuretype_api.get(path)
    try:
        return response.json()
    except json.JSONDecodeError:
        if response.status_code == 200:
            return response.text
        else:
            return abort(400)


@api_bp.route(
    f'/geoserver/rest/workspaces/{gs_workspace}/datastores/{pg_database}', methods=['GET'])
@api_bp.route(
    f'/geoserver/rest/workspaces/{gs_workspace}/datastores/{pg_database}.json', methods=['GET'])
@api_bp.route(f'/geoserver/rest/workspaces/{gs_workspace}/datastores/{pg_database}/<path:path>', methods=['GET'])
def get_datastore_proxy(path: str = '') -> str:
    response = datastore_api.get(path)
    try:
        return response.json()
    except json.JSONDecodeError:
        if response.status_code == 200:
            return response.text
        else:
            return abort(400)


@api_bp.route(f'/geoserver/rest/workspaces/{gs_workspace}', methods=['GET'])
@api_bp.route(f'/geoserver/rest/workspaces/{gs_workspace}.json', methods=['GET'])
@api_bp.route(f'/geoserver/rest/workspaces/{gs_workspace}/<path:path>', methods=['GET'])
def get_workspace_proxy(path: str = '') -> str:
    response = workspace_api.get(path)
    try:
        return response.json()
    except json.JSONDecodeError:
        if response.status_code == 200:
            return response.text
        else:
            return abort(400)


@api_bp.route('/geoserver/rest', methods=['GET'])
@api_bp.route('/geoserver/rest/<path:path>', methods=['GET'])
def get_geoserver_proxy(path: str = '') -> str:
    response = geoserver_api.get(path)
    try:
        return response.json()
    except json.JSONDecodeError:
        if response.status_code == 200:
            return response.text
        else:
            return abort(400)
