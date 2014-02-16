# marvelpy

A simple python wrapper for The Marvel Comics API.

# How to use

```
from marvelpy import Marvel

marvel = Marvel(api_key=YOUR_API_KEY, private_key=YOUR_PRIVATE_KEY)

# get characters
response = marvel.characters()
# response is a Response object which contains a server's response to an HTTP request
print response.text # Content of the response, in unicode.
print response.status_code # status code
print response.headers['etag'] # etag
# response.json() Returns the json-encoded content of a response, if any.

# get characters with filters
params = {'name': 'Cable'}
response = marvel.characters(params=params)
print response.text

# Get character by id
response = marvel.characters(id=1009214)
print response.text

# Get all comics containing specific character
response = marvel.characters(id=1009214, list_type='comics')
print response.text

# Get all comics containing specific character with filters
params = {'format': 'trade paperback'}
response = marvel.characters(id=1009214, list_type='comics', params=params)
print response.text

# get comics
response = marvel.comics()
print response.text

# get creators
response = marvel.creators()
print response.text

# get events
response = marvel.events()
print response.text

# get series
response = marvel.series()
print response.text

# get stories
response = marvel.stories()
print response.text

# make a request with etags
response = marvel.characters()
print response.text
print response.status_code # 200
etag = response.headers['etag']

response = marvel.characters(etag=etag)
print response.text # empty
print response.status_code # 304
```

For more information about available lists and parameters, please refer to The Marvel Comics API documentation - http://developer.marvel.com/docs.