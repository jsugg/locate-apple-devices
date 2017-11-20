from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from json import dumps
from subprocess import call
import urllib
import subprocess
from pyicloud import PyiCloudService
import os
import cStringIO
import sys  

user = os.environ['APPLE_DEVICES_ACCOUNT_USER']
password = os.environ['APPLE_DEVICES_ACCOUNT_PASSWORD']
my_env = os.environ
my_env['PYTHONIOENCODING'] = 'utf-8'

apple_devices_handy_tools = Flask(__name__)
api = Api(apple_devices_handy_tools)

ALLOWED_USERS = {
    "juanpedro": "penguino"
}

auth = HTTPBasicAuth()

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return ALLOWED_USERS.get(username) == password

class PlaySound(Resource):
  @auth.login_required
  def get(self, device_id):
    icloud_api = PyiCloudService(user, password)
    icloud_api.devices[device_id].play_sound()
    return "Beeping " + urllib.unquote(device_id)

class SendMessage(Resource):
  @auth.login_required
  def get(self, subject, message, sounds, device_id):
    if sounds != "True":
      sounds = "False"
    icloud_api = PyiCloudService(user, password)
    icloud_api.devices[device_id].display_message(subject, message, sounds)
    return "Message sent!"

api.add_resource(PlaySound, '/play_sound/<path:device_id>')
api.add_resource(SendMessage, '/send_message/<string:subject>/<string:message>/<string:sounds>/<path:device_id>')

if __name__ == '__main__':
  apple_devices_handy_tools.run(debug=False, host='0.0.0.0')
