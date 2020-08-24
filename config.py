import os

class BaseConfig(object):
    '''
    Base config class
    '''
    DEBUG = True
    TESTING = False
    WEBPACKEXT_MANIFEST_LOADER = "WebpackManifestFactory"
    WEBPACKEXT_MANIFEST_PATH = os.path.dirname(__file__) + '/app/dist/asset-manifest.json'

class Config(BaseConfig):
    """
    Production specific config
    """
    DEBUG = False

class DevConfig(BaseConfig):
    """
    Development environment specific configuration
    """
    DEBUG = True
    TESTING = True
