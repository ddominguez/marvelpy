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

    def get(self, url, params={}):
        if url.strip() == '':
            raise MarvelpyError('Resource URL is blank.')
        ts = str(time())
        hash = md5(ts + self._private_key + self._api_key)
        params.update({'apikey': self._api_key, 'ts': ts, 'hash': hash.hexdigest()})
        headers = {'Accept': 'application/json'}
        response = requests.get(url, params=params, headers=headers)
        return response.text

    def _resource_uri(self, api=None, id=None, list_type=None):
        uri = '%s/%s' % (self._base_url, api)
        if id is not None:
            uri = '%s/%s' % (uri, id)
            if list_type is not None:
                uri = '%s/%s' % (uri, list_type)
        return uri

    def characters(self, id=None, list_type=None, params={}):
        return self.get(self._resource_uri('characters', id, list_type), params)

    def comics(self, id=None, list_type=None, params={}):
        return self.get(self._resource_uri('comics', id, list_type), params)

    def creators(self, id=None, list_type=None, params={}):
        return self.get(self._resource_uri('creators', id, list_type), params)

    def events(self, id=None, list_type=None, params={}):
        return self.get(self._resource_uri('events', id, list_type), params)

    def series(self, id=None, list_type=None, params={}):
        return self.get(self._resource_uri('series', id, list_type), params)

    def stories(self, id=None, list_type=None, params={}):
        return self.get(self._resource_uri('stories', id, list_type), params)
