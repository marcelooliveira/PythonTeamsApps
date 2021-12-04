import os

class DefaultConfig:
  PORT = 3978
  APP_ID = os.environ.get("MicrosoftAppId", "")
  APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
  CONNECTION_NAME = os.environ.get("ConnectionName", "my-connection")
