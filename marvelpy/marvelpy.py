import requests
from hashlib import md5
from time import time

class MarvelpyError(Exception):
    pass

class Marvel(object):
    def __init__(self, api_key, private_key, version=1):
        self._api_key = api_key
        self._private_key = private_key
        self._base_url = 'http://gateway.marvel.com/v%s/public' % version

    def get(self, url, params={}, etag=None):
        if url.strip() == '':
            raise MarvelpyError('Resource URL is blank.')
        ts = str(time())
        hash = md5(ts + self._private_key + self._api_key)
        params.update({'apikey': self._api_key, 'ts': ts, 'hash': hash.hexdigest()})
        headers = {'Accept': 'application/json'}
        if etag:
            headers.update({'If-None-Match': etag})
        response = requests.get(url, params=params, headers=headers)
        return response

    def _resource_uri(self, api, id=None, list_type=None):
        uri = '%s/%s' % (self._base_url, api)
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

    def characters(self, **kwargs):
        id, list_type, params, etag = self._kwargs(kwargs)
        return self.get(self._resource_uri('characters', id, list_type), params, etag)

    def comics(self, **kwargs):
        id, list_type, params, etag = self._kwargs(kwargs)
        return self.get(self._resource_uri('comics', id, list_type), params, etag)

    def creators(self, **kwargs):
        id, list_type, params, etag = self._kwargs(kwargs)
        return self.get(self._resource_uri('creators', id, list_type), params, etag)

    def events(self, **kwargs):
        id, list_type, params, etag = self._kwargs(kwargs)
        return self.get(self._resource_uri('events', id, list_type), params, etag)

    def series(self, **kwargs):
        id, list_type, params, etag = self._kwargs(kwargs)
        return self.get(self._resource_uri('series', id, list_type), params, etag)

    def stories(self, **kwargs):
        id, list_type, params, etag = self._kwargs(kwargs)
        return self.get(self._resource_uri('stories', id, list_type), params, etag)
