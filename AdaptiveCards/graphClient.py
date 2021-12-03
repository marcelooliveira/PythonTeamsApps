from microsoftgraph.client import Client

class GraphClient():
    def __init__(self, token):
      if ((token == None) or (token.trim() == "")):
        raise Exception("SimpleGraphClient: Invalid token received.");

      self._token = token;

      # Get an Authenticated Microsoft Graph client using the token issued to the user.
      self.graphClient = Client("", "")

      #   def authProvider(done):
      #       done(null, this._token); // First parameter takes an error if you can't get an access token.
      # })()

    async def GetUserProfile(self):
      return await self.graphClient.get_me()

    def GetUserPhoto(self):
      # return await self.graphClient.get_me(). .get_me() .api('/me/photo/$value').get()
      return ""
