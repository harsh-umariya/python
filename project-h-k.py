import time
from plyer import notification

if __name__== "__main__":
    while True:
        notification.notify(
            title="Water Drink Now",
            message="please drink water right now",
            app_icon="",
            timeout=100
        )
        time.sleep(6)
