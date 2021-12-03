# import os
# from graphClient import GraphClient
# from botbuilder.core import TurnContext
# from botbuilder.core.teams import TeamsActivityHandler
# from Models.AdaptiveCardAction import createAuthResponse, createFetchResponse, createSubmitResponse, invokeTaskResponse, taskSubmitResponse
# # from Models.AdaptiveCardAction import ada

# class ActivityBot(TeamsActivityHandler):
#     def __init__(self, connectionName, applicationBaseUrl):
#         self.connectionName = connectionName;
#         self.applicationBaseUrl = applicationBaseUrl;

#     async def on_turn(self,turn_context:TurnContext):
#         if turn_context.activity.name == "tab/fetch":
#             # When the Bot Service Auth flow completes, turn_context will contain a magic code used for verification.
#             magicCode = ''
#             if turn_context.activity.value is not None and 'state' in turn_context.activity.value is not None:
#                 magicCode = turn_context.activity.value['state'] 

#             # Getting the tokenResponse for the user
#             tokenResponse = await turn_context.adapter.get_user_token(turn_context, os.environ.get("ConnectionName"), magicCode)

#             if (not tokenResponse) or (not tokenResponse.token):
#                 # Token is not available, hence we need to send back the auth response

#                 # Retrieve the OAuth Sign in Link.
#                 signInLink = await turn_context.adapter.get_oauth_sign_in_link(turn_context, os.environ.get("ConnectionName"))

#                 response = createAuthResponse(signInLink)

#                 # Generating and returning auth response.
#                 return response;

#             graphClient = GraphClient(tokenResponse.token);

#             profile = await graphClient.GetUserProfile()

#             userImage = await graphClient.GetUserPhoto()

#             return createFetchResponse(userImage, profile.displayName)
#         elif (turn_context.activity.name == "tab/submit"):
#             print('Trying to submit tab content');

#             adapter = turn_context.adapter
#             await adapter.signOutUser(turn_context, os.environ.get("ConnectionName"))

#             # Generating and returning submit response.
#             return createSubmitResponse();
#         elif (turn_context.activity.name == "task/fetch"):
#             # Task Module task/fetch
#             return invokeTaskResponse()
#         elif (turn_context.activity.name == "task/submit"):
#             # Task Module task/submit
#             return taskSubmitResponse()