# marvelpy

A simple python wrapper for The Marvel Comics API.

# How to use

```
from marvelpy import Marvel

marvel = Marvel(api_key=YOUR_API_KEY, private_key=YOUR_PRIVATE_KEY)

# get characters
result = marvel.characters()
print result # json formatted string

# get characters with filters
params = {'name': 'Cable'}
result = marvel.characters(params=params)
print result

# Get character by id
result = marvel.characters(id=1009214)
print result

# Get all comics containing specific character
result = marvel.characters(id=1009214, list_type='comics')
print result

# Get all comics containing specific character with filters
params = {'format': 'trade paperback'}
result = marvel.characters(id=1009214, list_type='comics', params=params)
print result

# get comics
result = marvel.comics()
print result

# get creators
result = marvel.creators()
print result

# get events
result = marvel.events()
print result

# get series
result = marvel.series()
print result

# get stories
result = marvel.stories()
print result
```

For more information about available lists and parameters, please refer to The Marvel Comics API documentation - http://developer.marvel.com/docs.