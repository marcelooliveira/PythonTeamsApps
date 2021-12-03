import requests
import json
import os
import base64
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
        })
      # Return the JSON result
      return user.json()

    def GetUserPhoto(self):
      # Send GET to /me/photo/$value
      photo_response = requests.get(
        '{0}/me/photo/$value'.format(graph_url),
        headers={
          'Authorization': 'Bearer {0}'.format(self._token)
        }, stream=True)
      photo_status_code = photo_response.status_code
      if photo_response.ok:
          photo = photo_response.raw.read()
          test = base64.b64encode(photo).decode('utf-8')
          # note we remove /$value from endpoint to get metadata endpoint
          metadata_response = requests.get(
            '{0}/me/photo/'.format(graph_url),
            headers={
              'Authorization': 'Bearer {0}'.format(self._token)
            })          
          content_type = metadata_response.json().get('@odata.mediaContentType', '')
      else:
          photo = ''
          content_type = ''

      return test