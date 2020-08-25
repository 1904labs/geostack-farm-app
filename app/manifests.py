import os
import json
from webpack_manifest.webpack_manifest import (
    WebpackManifest, 
    WebpackManifestEntry, 
    WebpackManifestFileError
)


class CraManifest(WebpackManifest):

    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "dist", "asset-manifest.json")
        static_root = os.path.dirname(path)
        data = self._read_manifest(path)
        super().__init__(path, data, '/dist/', static_root)
        self.main = WebpackManifestEntry(self._data['entrypoints'], self._static_url, self._static_root)


    def _read_manifest(self, path):
        if not os.path.isfile(path):
            raise WebpackManifestFileError('Path "{}" is not a file or does not exist'.format(path))

        if not os.path.isabs(path):
            raise WebpackManifestFileError('Path "{}" is not an absolute path to a file'.format(path))

        with open(path, 'r') as manifest_file:
            content = manifest_file.read()

        return json.loads(content)