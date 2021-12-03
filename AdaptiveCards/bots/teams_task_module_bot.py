# Copyright (c) Microsoft Corp. All rights reserved.
# Licensed under the MIT License.

import json
import os
from http import HTTPStatus

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
from Models.AdaptiveCardAction import createSubmitResponse, invokeTaskResponse, taskSubmitResponse
from graphClient import GraphClient
from microsoftgraph.client import Client

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

        profile = graphClient.GetUserProfile()

        userImage = graphClient.GetUserPhoto()

        return createFetchResponse(userImage, profile["displayName"])

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

# Card response for authentication
def createAuthResponse (signInLink):
    adaptive_card = {
        "status": HTTPStatus.OK,
        "body": {
            "tab": {
                "type": "auth",
                "suggestedActions": {
                    "actions": [
                        {
                            "type": "openUrl",
                            "value": signInLink,
                            "title": "Sign in to this app"
                        }
                    ]
                }
            },
        }
    }

    return CardFactory.adaptive_card(adaptive_card)

def  createFetchResponse(userImage, displayName):
    adaptive_card = {
        "status": HTTPStatus.OK,
        "body": {
            "tab": {
                "type": "continue",
                "value": {
                    "cards": [
                        {
                            # "card": getAdaptiveCardUserDetails(imageString, displayName),
                            "card": getAdaptiveCardUserDetails("", displayName),
                        },
                        {
                            "card": getAdaptiveCardSubmitAction(),
                        }
                    ]
                },
            },
        }
    }

    return CardFactory.adaptive_card(adaptive_card)

# Adaptive Card with user image, name and Task Module invoke action
def getAdaptiveCardUserDetails(image, name):
    adaptive_card = {
        "$schema": 'http://adaptivecards.io/schemas/adaptive-card.json',
        "body": [
            {
                "type": "ColumnSet",
                "columns": [
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "Image",
                                "url": "https://cdn.vox-cdn.com/thumbor/Ndb49Uk3hjiquS041NDD0tPDPAs=/0x169:1423x914/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/7342855/microsoftteams.0.jpg"
                                # "url": os.environ.get("ApplicationBaseUrl") + "/Images/profile-image.jpeg" 
                                #         if image and image != '' 
                                #         else "https://cdn.vox-cdn.com/thumbor/Ndb49Uk3hjiquS041NDD0tPDPAs=/0x169:1423x914/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/7342855/microsoftteams.0.jpg",
                                #         "size": "Medium"
                            }
                        ],
                        "width": "auto"
                    },
                    {
                        "type": "Column",
                        "items": [
                            {
                                "type": "TextBlock",
                                "weight": "Bolder",
                                "text": 'Hello: ' + name,
                                "wrap": True
                            },
                        ],
                        "width": "stretch"
                    }
                ]
            },
            {
                "type": 'ActionSet',
                "actions": [
                    {
                        "type": "Action.Submit",
                        "title": "Show Task Module",
                        "data": {
                            "msteams": {
                                "type": "task/fetch"
                            }
                        }
                    }
                ]
            }
        ],
        "type": 'AdaptiveCard',
        "version": '1.4'
    }
  
    return CardFactory.adaptive_card(adaptive_card)

# Adaptive Card showing sample text and Submit Action
def getAdaptiveCardSubmitAction():
    adaptiveCard = {
        "$schema": 'http://adaptivecards.io/schemas/adaptive-card.json',
        "body": [
            {
                "type": 'Image',
                "height": '300px',
                "width": '400px',
                "url": 'https://cdn.vox-cdn.com/thumbor/Ndb49Uk3hjiquS041NDD0tPDPAs=/0x169:1423x914/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/7342855/microsoftteams.0.jpg',
            },
            {
                "type": 'TextBlock',
                "size": 'Medium',
                "weight": 'Bolder',
                "text": 'tab/fetch is the first invoke request that your bot receives when a user opens an Adaptive Card tab. When your bot receives the request, it either sends a tab continue response or a tab auth response',
                "wrap": True,
            },
            {
                "type": 'TextBlock',
                "size": 'Medium',
                "weight": 'Bolder',
                "text": 'tab/submit request is triggered to your bot with the corresponding data through the Action.Submit function of Adaptive Card',
                "wrap": True,
            },
            {
                "type": 'ActionSet',
                "actions": [
                    {
                        "type": 'Action.Submit',
                        "title": 'Sign Out',
                    }
                ],
            }
        ],
        "type": 'AdaptiveCard',
        "version": '1.4'
    };

    return adaptiveCard