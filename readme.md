# Simple python-telegram-bot Template 

## Features

* Rotated file logging 
* Support for sentry 
* Mongo db 

## Setup
* Clone this repo 
* Create a .env file and add in your 
    * Telegram BOT api token 
    * Mongo db uri and 
    * Sentry ingest link

```
TOKEN=0000000000:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
DBURI=mongodb+srv://<USER>:<PASSWORD>@<CLUSTER>.gkazp.mongodb.net
SENTRY=https://XX000000XX0000X0XX00X00000XXXX0X@X000000.ingest.sentry.io/0000000
```
* Run the script
```py
python main.py
```

* Send the bot a /start and check if you get a " hi there im alive " message back
