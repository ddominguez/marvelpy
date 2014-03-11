import requests
from hashlib import md5
from time import time


class MarvelpyError(Exception):
    pass


class Marvel(object):
    def __init__(self, api_key, private_key, version=1):
        self._api_key = api_key
        self._private_key = private_key
        self._base_uri = 'http://gateway.marvel.com/v%s/public' % version
        self._request_uri = None

    def get(self, uri, params={}, etag=None):
        if uri.strip() == '':
            raise MarvelpyError('Resource URI is blank.')
        if not uri.startswith(self._base_uri):
            raise MarvelpyError('Invalid Marvel API URI.')
        self._request_uri = uri
        ts = str(time())
        hash = md5(ts + self._private_key + self._api_key)
        params.update({'apikey': self._api_key, 'ts': ts, 'hash': hash.hexdigest()})
        headers = {'Accept': 'application/json'}
        if etag:
            headers.update({'If-None-Match': etag})
        response = requests.get(uri, params=params, headers=headers)
        return response

    def _resource_uri(self, api, id=None, list_type=None):
        uri = '%s/%s' % (self._base_uri, api)
        if id is not None:
            uri = '%s/%s' % (uri, id)
            if list_type is not None:
                uri = '%s/%s' % (uri, list_type)
        return uri

    def _kwargs(self, kwargs):
        kw = {
            'id': None,
            'list_type': None,
            'params': {},
            'etag': None
        }

        for k in kw.keys():
            if k in kwargs:
                kw[k] = kwargs[k]

        return (kw['id'], kw['list_type'], kw['params'], kw['etag'])

    def _get_response(self, collection, kwargs):
        id, list_type, params, etag = self._kwargs(kwargs)
        return self.get(self._resource_uri(collection, id, list_type), params, etag)

    def characters(self, **kwargs):
        return self._get_response('characters', kwargs)

    def comics(self, **kwargs):
        return self._get_response('comics', kwargs)

    def creators(self, **kwargs):
        return self._get_response('creators', kwargs)

    def events(self, **kwargs):
        return self._get_response('events', kwargs)

    def series(self, **kwargs):
        return self._get_response('series', kwargs)

    def stories(self, **kwargs):
        return self._get_response('stories', kwargs)

    @property
    def _image_metadata(self):
        return {
            'portrait': {
                'small': {
                    'width': 50,
                    'height': 75
                },
                'medium': {
                    'width': 100,
                    'height': 150
                },
                'xlarge': {
                    'width': 150,
                    'height': 225
                },
                'fantastic': {
                    'width': 168,
                    'height': 252
                },
                'uncanny': {
                    'width': 300,
                    'height': 450
                },
                'incredible': {
                    'width': 216,
                    'height': 324
                }
            },
            'standard': {},
            'landscape': {},
            'full': {}
        }

    def image(self, image_object, type, size):
        if set(['path', 'extension']) != set(image_object.keys()):
            raise MarvelpyError('Marvel image object missing path or extension.')

        if type not in self._image_metadata:
            raise MarvelpyError('Invalid image type.')

        if size not in self._image_metadata[type]:
            raise MarvelpyError('Invalid image size.')

        image = {
            'url': '%s/%s_%s.%s' % (image_object['path'], type, size, image_object['extension']),
            'width': self._image_metadata[type][size]['width'],
            'height': self._image_metadata[type][size]['height']
        }
        return image
