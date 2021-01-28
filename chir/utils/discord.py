import requests
from configs import settings


class DiscordBot:
    def __init__(self, webhook):
        self.webhook = webhook

    def send_message(self, message):
        msg = "**{}**: {}".format(settings.SERVER, message)
        requests.post(self.webhook, json={"content": msg})


discord = DiscordBot(settings.WEBHOOK_URL)
