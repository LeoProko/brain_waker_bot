import threading
import json

from handler import handler
from sender import sender


def init_subscribers_data():
    with open("subscribers.json", "w", encoding="utf-8") as file:
        json.dump({"subscribers": []}, file, indent=4)


def run_bot():
    init_subscribers_data()

    handler_thread = threading.Thread(target=handler)
    sender_thread = threading.Thread(target=sender)

    handler_thread.start()
    sender_thread.start()

    handler_thread.join()
    sender_thread.join()


if __name__ == "__main__":
    run_bot()
