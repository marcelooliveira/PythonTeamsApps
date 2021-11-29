#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    MicrosoftAppType = os.environ.get("MicrosoftAppType", "MultiTenant")
    MicrosoftAppId = os.environ.get("MicrosoftAppId", "477862ce-734c-49c7-97f8-84699d62fe15")
    MicrosoftAppPassword = os.environ.get("MicrosoftAppPassword", "The_power_of_now_2")
    MicrosoftAppTenantId = ""
    PORT = 3978
    CONNECTION_NAME = os.environ.get("ConnectionName", "my-connection")
    APP_BASE_URL = os.environ.get("ApplicationBaseUrl", "https://824d-2804-14c-bf2f-a532-ed0e-b089-875b-e506.ngrok.io")
