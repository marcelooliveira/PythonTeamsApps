#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

MicrosoftAppId = os.environ.get("MicrosoftAppId", "5371a93b-6337-4dca-ac05-5bd98dee234d")
MicrosoftAppPassword = os.environ.get("MicrosoftAppPassword", "-qX7Q~jw42rHBpq3sRUPUlj-H1MeDCclwBcAP")
ConnectionName = os.environ.get("ConnectionName", "my-connection")
# ApplicationBaseUrl = os.environ.get("ApplicationBaseUrl", "https://adaptive-cards-function-app.azurewebsites.net")
ApplicationBaseUrl = os.environ.get("ApplicationBaseUrl", "https://f82a-2804-14c-bf2f-a532-d87-9191-6c7d-4451.ngrok.io")

class DefaultConfig:
  MicrosoftAppId = os.environ.get("MicrosoftAppId", "5371a93b-6337-4dca-ac05-5bd98dee234d")
  MicrosoftAppPassword = os.environ.get("MicrosoftAppPassword", "-qX7Q~jw42rHBpq3sRUPUlj-H1MeDCclwBcAP")
  ConnectionName = os.environ.get("ConnectionName", "my-connection")
  # ApplicationBaseUrl = os.environ.get("ApplicationBaseUrl", "https://adaptive-cards-function-app.azurewebsites.net")
  ApplicationBaseUrl = os.environ.get("ApplicationBaseUrl", "https://f82a-2804-14c-bf2f-a532-d87-9191-6c7d-4451.ngrok.io")
  PORT = 3978
  APP_ID = os.environ.get("MicrosoftAppId", "5371a93b-6337-4dca-ac05-5bd98dee234d")
  APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "-qX7Q~jw42rHBpq3sRUPUlj-H1MeDCclwBcAP")
  CONNECTION_NAME = os.environ.get("ConnectionName", "my-connection")
  BASE_URL = os.environ.get("ApplicationBaseUrl", "https://f82a-2804-14c-bf2f-a532-d87-9191-6c7d-4451.ngrok.io")
