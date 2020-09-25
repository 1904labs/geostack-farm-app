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
                "features",
                ft_name
            ]
        },
        "latLonBoundingBox": {
            "maxx": -68.036694,
            "maxy": 49.211179,
            "minx": -124.571077,
            "miny": 25.404663,
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