# Handy tool to help you locate your Apple devices
A very simple API that makes it easy to locate a device. The idea behind it, is to avoid wasting time by walking around the office asking everyone for the device. Especially useful, when working at a company that develops for mobile, and share MANY devices amongst developers.

The API is Dockerized and ready to go.

## Features
* Send messages.
* Plays sounds.
* It uses [oauth2_proxy](https://github.com/bitly/oauth2_proxy) for Google account authentication (you can change it to whatever you use), Nginx as reverse proxy, and the [PyiCloud](https://github.com/picklepete/pyicloud) CLI.

The flow goes like this:
Your API request -> Nginx -> oauth2_proxy -> Nginx -> Application Server (gunicorn) -> Python API (Flask)

## Configuration
iCloud account credentials, allowed Google account domains (as much as you want), and Google API details, are environment variables: 

Create a `.env` file with:
```
PORT=80
ALLOWED_DOMAINS=[\"<yourdomain.com>\",\"<if-you-have-a-second-domain.com>\"]
APPLE_DEVICES_ACCOUNT_USER=your@email.com
APPLE_DEVICES_ACCOUNT_PASSWORD=your_password
OAUTH2_PROXY_CLIENT_ID=<google api client id>
OAUTH2_PROXY_CLIENT_SECRET=<google api client secret>
OAUTH2_PROXY_COOKIE_SECRET=<a random secret string here>
OAUTH2_PROXY_COOKIE_DOMAIN=.<your domain>
OAUTH2_PROXY_REDIRECT_URL=<your callback url>
```

For the last two lines, you could use something like this in a development environment:
```
OAUTH2_PROXY_COOKIE_DOMAIN=.nip.io
OAUTH2_PROXY_REDIRECT_URL=http://127.0.0.1.nip.io:8080/oauth2/callback
```

For the Google API credentials, just go to [Google developers console](https://console.developers.google.com/apis/) and create the credentials. Then, just copy/paste them into your .env file.
```
OAUTH2_PROXY_CLIENT_ID
OAUTH2_PROXY_CLIENT_SECRET
```

To run it locally:
`docker run -i -p 8080:80 --env-file .env apple-devices-locator`

You can reach the API in the port 8080. Remember that you must be logged into a google account, from one of the allowed domains. If you're not logged in, it'll ask you to loggin.

To move to production, it'll depend on how you're gonna do that (Kubernetes, Heroku, etc, ...).
Using deis, it should be as simple as this:
```
deis config:push
git push deis master
```

## Play sound
POST request (form-data)
```
device_id=<device id from you apple device>
```
[https://imgur.com/a/jGChT](https://imgur.com/a/jGChT)

Note: it's the device id, NOT the device udid

## Send Message
POST request (form-data)
```
device_id=<device id from you apple device>
title=<the title of your message>
message=<your text>
beep=<True/False>
```
If `beep=True` the device will make some LOUD noise until someone touches the home button.

[https://imgur.com/a/jaJSK](https://imgur.com/a/jaJSK)

## Contributions
For now, I think this is what we need. Any contributions are welcome!
