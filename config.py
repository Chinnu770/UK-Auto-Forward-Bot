from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "4ed1b0d3f9394927baac66bcae1a4d53")
      API_ID = int(getenv("API_ID", 29219263))
      AS_COPY = True if getenv("AS_COPY", True) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "6976746689:AAGoPOufnSNOM33iSjBcuxr1KEWpk1hEwk8")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001749307905:-1001952248822").replace("\n", " ").split(' '))
