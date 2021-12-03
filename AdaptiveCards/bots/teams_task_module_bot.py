# Copyright (c) Microsoft Corp. All rights reserved.
# Licensed under the MIT License.

import json
import os

from botbuilder.core import (
    CardFactory,
    MessageFactory,
    TurnContext,
)
from botbuilder.schema import HeroCard, Attachment, CardAction
from botbuilder.schema.teams import (
    TaskModuleMessageResponse,
    TaskModuleRequest,
    TaskModuleResponse,
    TaskModuleTaskInfo,
    TabRequest,
    TabSubmit
)
from botbuilder.core.teams import TeamsActivityHandler

from config import DefaultConfig
from Models.AdaptiveCardAction import createAuthResponse, createFetchResponse, createSubmitResponse, invokeTaskResponse, taskSubmitResponse
from graphClient import GraphClient

class TeamsTaskModuleBot(TeamsActivityHandler):
    def __init__(self, config: DefaultConfig):
        self.__base_url = config.BASE_URL

    async def on_teams_tab_fetch(  # pylint: disable=unused-argument
        self, turn_context: TurnContext, tab_request: TabRequest
    ):
        """
        Override this in a derived class to provide logic for when a tab is fetched.
        :param turn_context: A context object for this turn.
        :param tab_request: The tab invoke request value payload.
        :returns: A Tab Response for the request.
        """
        # When the Bot Service Auth flow completes, turn_context will contain a magic code used for verification.
        magicCode = ''
        if turn_context.activity.value is not None and 'state' in turn_context.activity.value is not None:
            magicCode = turn_context.activity.value['state'] 

        # Getting the tokenResponse for the user
        tokenResponse = await turn_context.adapter.get_user_token(turn_context, os.environ.get("ConnectionName"), magicCode)

        if (not tokenResponse) or (not tokenResponse.token):
            # Token is not available, hence we need to send back the auth response

            # Retrieve the OAuth Sign in Link.
            signInLink = await turn_context.adapter.get_oauth_sign_in_link(turn_context, os.environ.get("ConnectionName"))

            # Generating and returning auth response.
            return createAuthResponse(signInLink)

        graphClient = GraphClient(tokenResponse.token);

        profile = await graphClient.GetUserProfile()

        userImage = await graphClient.GetUserPhoto()

        return createFetchResponse(userImage, profile.displayName)

    async def on_teams_tab_submit(  # pylint: disable=unused-argument
        self, turn_context: TurnContext, tab_submit: TabSubmit
    ):
        """
        Override this in a derived class to provide logic for when a tab is submitted.
        :param turn_context: A context object for this turn.
        :param tab_submit: The tab submit invoke request value payload.
        :returns: A Tab Response for the request.
        """
        adapter = turn_context.adapter
        await adapter.signOutUser(turn_context, os.environ.get("ConnectionName"))

        # Generating and returning submit response.
        return createSubmitResponse();

    async def on_teams_task_module_fetch(
        self, turn_context: TurnContext, task_module_request: TaskModuleRequest
    ) -> TaskModuleResponse:
        """
        Called when the user selects an options from the displayed HeroCard or
        AdaptiveCard.  The result is the action to perform.
        """

        return invokeTaskResponse()

    async def on_teams_task_module_submit(
        self, turn_context: TurnContext, task_module_request: TaskModuleRequest
    ) -> TaskModuleResponse:
        """
        Called when data is being returned from the selected option (see `on_teams_task_module_fetch').
        """

        return taskSubmitResponse()
