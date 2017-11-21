# Handy Tool to locate Apple Devices

A very simple API that makes it easier to locate a device. The idea behid it, is to avoid wasting time walking around the office asking everyone for the device.

## Features
* Send message
* Play sound

## Configuration
First install all dependencies.
	-- pip install -r requirements.txt

iCloud account's credentials are environment variables: 
	-- APPLE_DEVICES_ACCOUNT_USER=your@email.com
	-- APPLE_DEVICES_ACCOUNT_PASSWORD=your_password

API authentication (basic auth). You just need to edit the file **handy_tools_apple_devices.py**, and set whatever you want. You can specify more than one user.
	-- ALLOWED_USERS = {
    		"user": "password"
	}	

## Usage
Note that every string containing spaces or special characters must be *urlencoded*. You can always use the encodeURI() in JavaScript, urllib.quote_plus in Python, or whatever suits you better. You can use [this website](https://www.urlencoder.org/) for testing.

Start the server
	-- python handy_tools_apple_devices.py

* Send a message
	-- curl -u user:password --basic http://localhost:5000/send_message/<title>/<message>/<play_sound>/<url_encoded_device_id>

Example:
	-- curl -u user:password --basic http://localhost:5000/send_message/Message/Hi%2C%20I%27m%20looking%20for%20this%20device.%20John/False/LArHgLz00DPUNt6bjUnMvIPyAdZhz%2FHtlAq0ASCo%2BsCuHF5wOmDYuuHYVNSUzmWW

This send a pop-up window with title "Message", message "Hi, I'm looking for this device. John", without beeping (play_sound=False), to the device with id=LArHgLz00DPUNt6bjUnMvIPyAdZhz/HtlAq0ASCo+sCuHF5wOmDYuuHYVNSUzmW

* Play sound
	-- curl -u user:password --basic http://localhost:5000/play_sound/<url_encoded_device_id>

Example:
	-- curl -u user:password --basic http://localhost:5000/play_sound/LArHgLz00DPUNt6bjUnMvIPyAdZhz%2FHtlAq0ASCo%2BsCuHF5wOmDYuuHYVNSUzmW

## Notes
* For now, I think this is all we need. If you think we could add something useful, you're free to contribute. 
