import os


class Credentials:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")  # from @botfather
    API_ID = int(os.environ.get("API_ID"))  # from https://my.telegram.org/apps
    API_HASH = os.environ.get("API_HASH")  # from https://my.telegram.org/apps
    # Banned Unwanted Members..
    BANNED_USERS = {int(x) for x in os.environ.get("BANNED_USERS","").split()}

# Okay 🤣
