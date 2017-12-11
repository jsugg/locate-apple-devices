from flask import Flask, request
from flask_restful import Resource, Api
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

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

apple_devices_handy_tools = Flask(__name__)
api = Api(apple_devices_handy_tools)

class PlaySound(Resource):
  def post(self):
    if not 'device_id' in request.form:
      return "Missing device id.", 400

    device_id = request.form['device_id']
    try:
      icloud_api = PyiCloudService(user, password)
      icloud_api.devices[device_id].play_sound()
      return "Beeping " + device_id, 200
    except:
      return 'Could not send the beep.', 400

class SendMessage(Resource):
  def post(self):
    subject = request.form['title'] if 'title' in request.form else 'Subject'
    message = request.form['message'] if 'message' in request.form else 'Message'
    beep = request.form['beep'] if 'beep' in request.form else False
    device_id = request.form['device_id'] if 'device_id' in request.form else False

    if not device_id:
      return 'Missing device id.', 400
    
    try:
      icloud_api = PyiCloudService(user, password)
      icloud_api.devices[device_id].display_message(subject, message, beep)
      return 'Message sent to device id: ' + device_id, 200
    except:
      return 'Could not send the message.', 400

api.add_resource(PlaySound, '/beeps/')
api.add_resource(SendMessage, '/messages/')

if __name__ == '__main__':
  apple_devices_handy_tools.run(debug=False, host='0.0.0.0', port=3010)
