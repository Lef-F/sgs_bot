# Home finder

I grew tired of refreshing the SGS webpage for new appartments, so I made a script to send direct link notifications through PushBullet whenever an interesting appartment ad is posted.

## Installation

Get a PushBullet API key and store it your `api.key` file.

Browse with Chrome to SGS website and to the [ads page](https://marknad.sgsstudentbostader.se).
Press F12 to get the Chrome Dev Tools and navigate to the `Network` tab.
Configure the filters you wish and hit *search*.
Then on the Dev Tools a `POST` request named `SearchServiceHandler.ashx` should show up.
Right click on it, and from the `Copy` menu select `Copy as cURL (Bash)`.
Paste this into your `requests.curl` file.

Run `pip install pushbullet tinydb`.

Running `python3 sgs_bot.py` should create an `sgs_db.json` file and if any results are available, you should get notifications for each one on PushBullet.

Now you can add it to your `crontab -e` and run it every minute or so.

Follow the links and apply for em! Enjoy your stay!

## ToDos

Make it simple, stupid.
