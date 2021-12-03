import requests
import json
import os
from microsoftgraph.client import Client

graph_url = 'https://graph.microsoft.com/v1.0'

class GraphClient():
    def __init__(self, token):
      if ((token == None) or (token.strip() == "")):
        raise Exception("SimpleGraphClient: Invalid token received.");

      self._token = token;

      # Get an Authenticated Microsoft Graph client using the token issued to the user.
      self.graphClient = Client(os.environ.get("MicrosoftAppId"), os.environ.get("MicrosoftAppPassword"))

    def GetUserProfile(self):
      # Send GET to /me
      user = requests.get(
        '{0}/me'.format(graph_url),
        headers={
          'Authorization': 'Bearer {0}'.format(self._token)
        }
        # ,
        # params={
        #   '$select': 'displayName,mail,mailboxSettings,userPrincipalName'
        # }
        )
      # Return the JSON result
      return user.json()

    def GetUserPhoto(self):
      # return await self.graphClient.get_me(). .get_me() .api('/me/photo/$value').get()
      return ""
