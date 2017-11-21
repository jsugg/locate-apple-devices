# Handy Tools for Apple Devices

A micro API that makes it easier to locate a device. The idea is to avoid wasting time walking around the office asking everyone for the device.

## Features
* Send message
* Play sound

## Configuration
iCloud account's credentials are environment variables: APPLE_DEVICES_ACCOUNT_USER, APPLE_DEVICES_ACCOUNT_PASSWORD

API authentication (basic auth). You just need to edit the file **handy_tools_apple_devices.py**
	ALLOWED_USERS = {
    		"user": "password"
	}	

## Usage
Note that every string containing spaces or special characters must be *urlencoded*. You can always use the encodeURI() in JavaScript, urllib.quote_plus in Python, or whatever suits you better. You can use [this website](https://www.urlencoder.org/) for testing.

* Send message
	http://localhost:5000/send_message/<title>/<message>/<play_sound>/<url_encoded_device_id>
Example:
	http://localhost:5000/send_message/Hola/Mensaje/False/LArHgLz00DPUNt6bjUnMvIPyAdZhz%2FHtlAq0ASCo%2BsCuHF5wOmDYuuHYVNSUzmWW
This send a pop-up window with title "Hola", message "Mensaje", without beeping (play_sound=False), to the device with id=LArHgLz00DPUNt6bjUnMvIPyAdZhz/HtlAq0ASCo+sCuHF5wOmDYuuHYVNSUzmW

* Play sound
	http://localhost:5000/play_sound/<url_encoded_device_id>
Example:
	http://localhost:5000/play_sound/LArHgLz00DPUNt6bjUnMvIPyAdZhz%2FHtlAq0ASCo%2BsCuHF5wOmDYuuHYVNSUzmW

## Notes
* For now, I think this is all we need. If you think we need something more, you're free to contribute. 
