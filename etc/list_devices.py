from pyicloud import PyiCloudService
import os

user = os.environ['APPLE_DEVICES_ACCOUNT_USER']
password = os.environ['APPLE_DEVICES_ACCOUNT_PASSWORD']
api = PyiCloudService(user, password)
devices = api.account.devices

print(str(len(devices)) + " registered devices. Details:\n")
print ("Name\tModel Name\tModel\tOS\tSerial Number\tIMEI\tudid")

for i in devices:
  print (i[u'name'] + '\t' + i[u'modelDisplayName'] + '\t' + i[u'model'] + '\t' + i[u'osVersion'] + '\t' + i[u'serialNumber'].replace('\u25cf', '') + '\t' + i[u'imei'] + '\t' + i[u'udid'])

print ('\n\nUnique ids\n')

for k,v in api.devices.items():
  print(str(v) + '\t' + str(k))
