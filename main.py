import os
import string
import random

def respond (request): #flask.request
  request_json = request.get_json()

  # check if the name parameter is in the query parameter
  if request.args and 'name' in request.args:
    name = request.args.get('name')
  elif request_json and 'name' in request_json:
    name = request_json['name']
  else: 
    name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 100))

  return f"{name}!"
