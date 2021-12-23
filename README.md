# Brain waker bot
*Wake your brain up*


## What does the bot do?
This Telegram bot sends a random easy task every one to three hours to test your brain for fatigue.

You can test my bot by yourself https://t.me/brain_waker_bot

Now this bot check your answer, just send questions :(


## Structure
- `handler.py`
    - Handle users requests
- `sender.py`
    - Send a task for subscribers from `subscreibers.json` where they are
- `subscribers.json`
    - The Json file that contains the `chat_id` of the subscribers in the list


## Technology
I used `pyTelegramBotApi`, `Docker` and `WathcTower` to implement the bot and the infrastructure around it.


## CI/CD
This bot runs on my own server, using `WatchTower` to check for updates to the `Docker` image. The `Docker` image is updated each time a new `release` occurs in this `GitHub` repository.

At each `push` to this repository, the `CI` system is run to lint `python` code.
