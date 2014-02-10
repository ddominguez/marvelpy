# marvelpy

A simple python wrapper for The Marvel Comics API.

# How to use

marvel = Marvel(api_key=YOUR_API_KEY, private_key=YOUR_PRIVATE_KEY)

**Get character by name**
params = {'name': 'Cable'}
result = marvel.characters(params=params)
print result # json formatted string