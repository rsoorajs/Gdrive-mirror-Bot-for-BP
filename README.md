# GDrive Mirror Bot
This is a fork from [here](https://github.com/atulkadian/gdrivemirror_bot).

The original bot is up and running [here](https://t.me/gdrivemirror_bot).

![​](https://telegra.ph/file/6bbe2759c304a5b834ee2.jpg)

## Features:
- Create GDrive Mirror of direct download links.
- Create GDrive Mirror of videos from [1000+ websites](http://rg3.github.io/youtube-dl/supportedsites.html) including YouTube.
- Custom filename support.
- Extract high quality audio from youtube videos.

## Requirements:
- python >=2.7, <3.0
- Install all requirements using `pip install -r requirements.txt`

## Bringing it online:
- Put your credentials (Bot Token, Client ID, Client secret, Drive folder ID and TG chat id) in `credentials.py` file.
- Run command `python bot.py`
- Complete the authentication to generate auth-token.

## Deploy to Heroku

You have to create the auth_token.txt file by runnig the bot on your local machine for the first time.
Then upload the auth_token.txt file to your git repo and then deploy it to heroku.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

