import os
from . import api
from flask import jsonify
from flask_restx import Resource, Model, fields

geoserver_model = Model('Geoserver', {
    'geoserver': fields.String(description='The url of a geoserver')
})

@api.rp.route('/geoserver')
class Geoserver(Resource):

    @api.rp.doc('get_geoserver')
    #@api.rp.marshal_with(geoserver_model)
    def get(self):
        geoserver = getattr(
            self, '_geoserver',
            os.environ.get('GEOSERVER_URL', "http://localhost:8000")
        )
        return jsonify({"geoserver": geoserver})
