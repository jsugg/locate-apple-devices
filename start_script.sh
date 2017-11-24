exec gunicorn --workers 3 --bind unix:handy_tools_apple_devices.sock -m 007 wsgi:handy_tools_apple_devices
