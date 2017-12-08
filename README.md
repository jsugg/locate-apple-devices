# Handy Tool to help you locate Apple Devices

A very simple API that makes it easier to locate a device. The idea behid it, is to avoid wasting time walking around the office asking everyone for the device. Something extremely useful, when working at a company that develops for mobile, and share MANY devices amongst developers.

The API is Dockerized and ready to go.

## Features
* Send messages.
* Plays sounds.
* Utilizes oauth2_proxy for google account authentication (you can change it to whatever you want).

## Configuration
Create a `.env` file with:

iCloud account's credentials are environment variables: 
```
PORT=80
ALLOWED_DOMAINS=[\"<yourdomain.com>\",\"<if-you-have-a-seccond-domain.com>\"]
APPLE_DEVICES_ACCOUNT_USER=your@email.com
APPLE_DEVICES_ACCOUNT_PASSWORD=your_password
OAUTH2_PROXY_CLIENT_ID=<google's api client id>
OAUTH2_PROXY_CLIENT_SECRET=<google api's clien secret>
OAUTH2_PROXY_COOKIE_SECRET=<a random secret string here>
OAUTH2_PROXY_COOKIE_DOMAIN=.<your domain>
OAUTH2_PROXY_REDIRECT_URL=<your callback url>
```

The last two lines, in a development environment, could be something like:
```
OAUTH2_PROXY_COOKIE_DOMAIN=.nip.io
OAUTH2_PROXY_REDIRECT_URL=http://127.0.0.1.nip.io:8080/oauth2/callback
```

For the API credentials, just go to [Google developers console](https://console.developers.google.com/apis/) and create credentials. Then, just copy/paste them in your .env file.
```
OAUTH2_PROXY_CLIENT_ID
OAUTH2_PROXY_CLIENT_SECRET
```

To start it locally:
`docker run -i -p 8080:80 --env-file .env apple-devices-locator`

To deploy to production, it'll depend on how you're gonna do that (deis, heroku, ...).

You can reach your API in the port 8080. Remember that you must be logged into a google account, from the allowed domains list. If you're not, it'll reject the request.

## Play sound
POST request. form-data
```
device_id=<device id from you apple device>
```
![Beeping a device](https://imgur.com/a/jGChT)

## Send Message
POST request. form-data
```
device_id=<device id from you apple device>
title=<the title of your message>
message=<your text>
beep=<True/False>
```
If `beep=True` the device will make some LOUD noise until someone touches the home button.

![Sending a message to a device](https://imgur.com/a/jaJSK)

## Contributions
For now, I think this is what we need. Any contributions are welcome!
