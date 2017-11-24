from pyicloud import PyiCloudService
import os

user = os.environ['APPLE_DEVICES_ACCOUNT_USER']
password = os.environ['APPLE_DEVICES_ACCOUNT_PASSWORD']
api = PyiCloudService(user, password)
devices = api.account.devices

print(str(len(devices)) + " registered devices. Details:\n")
print ("Name\tModel Name\tModel\tOS\tSerial Number\tIMEI\tudid")

# Devices with iOS >=8
for i in devices:
  print (i[u'name'] + '\t' + i[u'modelDisplayName'] + '\t' + i[u'model'] + '\t' + i[u'osVersion'] + '\t' + i[u'serialNumber'].replace('\u25cf', '') + '\t' + (i['imei'] if 'imei' in i else '-') + '\t' + i[u'udid'])

# All devices ids, all iOS versions.
print ('\n\nUnique ids\n')
for k,v in api.devices.items():
  print(str(v) + '\t' + str(k))

print ('\n\nA few more attributes for the devices on the first list')

# List a few more attributes for >= iOS 8 devices. Unordered
for i in api.account.devices:
  for key, value in i.iteritems():
    print key, '\t',  value
  print('\n')
