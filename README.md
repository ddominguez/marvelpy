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
# if data has not changed, status code will be 304 with empty content
# if data has changed, status code will be 200 with updated content
print response.text
print response.status_code

# get data using marvel api resource uri
# will also accept params and etag arguments
# > response = marvel.get(uri='RESOURCE_URI', params=DICT_OF_FILTERS, etag=ETAG_STRING)
response = marvel.get('http://gateway.marvel.com/v1/public/comics/39770')
print response.text

# get thumbail and image urls
# > marvel.image(IMAGE_OBJECT, IMAGE_TYPE, IMAGE_SIZE)
# types: portrait, standard, landscape, full
# portrait|standard|landscape sizes: small, medium, large, xlarge, fantastic, uncanny, incredible, amazing
# full sizes: detail, full
# see more sizes at http://developer.marvel.com/documentation/images
response = marvel.characters(id=1009214)
result = response.json()['data']['results'][0]
thumbnail = marvel.image(result['thumbnail'], 'standard', 'medium')
fullimage = marvel.image(result['thumbnail'], 'full', 'full')
print thumbnail
# {'url': u'http://i.annihil.us/u/prod/marvel/i/mg/3/90/526165df2b584/standard_medium.jpg', 'width': 100, 'height': 100}
print fullimage
# {'url': u'http://i.annihil.us/u/prod/marvel/i/mg/3/90/526165df2b584.jpg'}
# NOTE: full images do not return width or height
```

For more information about available lists and parameters, please refer to The Marvel Comics API documentation - http://developer.marvel.com/docs.