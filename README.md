# marvelpy

A simple python wrapper for The Marvel Comics API.

# How to use

```
marvel = Marvel(api_key=YOUR_API_KEY, private_key=YOUR_PRIVATE_KEY)

# get character by name
params = {'name': 'Cable'}
result = marvel.characters(params=params)
print result # json formatted string

# Get character by id
result = marvel.characters(id=1009214)
print result

# Get all comics containing specific character
result = marvel.characters(id=1009214, list_type='comics')
print result
```