import os

from botbuilder.core import (
    TurnContext,
)
from botbuilder.schema.teams import (
    TaskModuleRequest,
    TaskModuleResponse,
    TabRequest,
    TabSubmit
)
from botbuilder.core.teams import TeamsActivityHandler
from Models.AdaptiveCards import createAuthResponse, createFetchResponse, createSubmitResponse, invokeTaskResponse, taskSubmitResponse

from graphClient import GraphClient

class TeamsTaskModuleBot(TeamsActivityHandler):
    async def on_teams_tab_fetch(  # pylint: disable=unused-argument
        self, turn_context: TurnContext, tab_request: TabRequest
    ):
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

        profile = graphClient.GetUserProfile()

        userImage = graphClient.GetUserPhoto(profile["id"])

        return createFetchResponse(userImage, profile["displayName"])

    async def on_teams_tab_submit(  # pylint: disable=unused-argument
        self, turn_context: TurnContext, tab_submit: TabSubmit
    ):
        adapter = turn_context.adapter
        await adapter.sign_out_user(turn_context, os.environ.get("ConnectionName"))

        # Generating and returning submit response.
        return createSubmitResponse();

    async def on_teams_task_module_fetch(
        self, turn_context: TurnContext, task_module_request: TaskModuleRequest
    ) -> TaskModuleResponse:
        return invokeTaskResponse()

    async def on_teams_task_module_submit(
        self, turn_context: TurnContext, task_module_request: TaskModuleRequest
    ) -> TaskModuleResponse:
        return taskSubmitResponse()

