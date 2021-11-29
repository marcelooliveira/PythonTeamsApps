#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

MicrosoftAppId = os.environ.get("MicrosoftAppId", "5371a93b-6337-4dca-ac05-5bd98dee234d")
MicrosoftAppPassword = os.environ.get("MicrosoftAppPassword", "-qX7Q~jw42rHBpq3sRUPUlj-H1MeDCclwBcAP")
ConnectionName = os.environ.get("ConnectionName", "my-connection")
ApplicationBaseUrl = os.environ.get("ApplicationBaseUrl", "https://adaptive-cards-function-app.azurewebsites.net")

class DefaultConfig:
    """ Bot Configuration """
  MicrosoftAppId = os.environ.get("MicrosoftAppId", "5371a93b-6337-4dca-ac05-5bd98dee234d")
  MicrosoftAppPassword = os.environ.get("MicrosoftAppPassword", "-qX7Q~jw42rHBpq3sRUPUlj-H1MeDCclwBcAP")
  ConnectionName = os.environ.get("ConnectionName", "my-connection")
  ApplicationBaseUrl = os.environ.get("ApplicationBaseUrl", "https://adaptive-cards-function-app.azurewebsites.net")
