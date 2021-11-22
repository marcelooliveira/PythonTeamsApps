from flask import request
import msal
import os
import json

app = msal.ConfidentialClientApplication(
    client_id=os.environ.get("ClientId"),
    authority="https://login.microsoftonline.com/" + os.environ.get("TenantId"),
    client_credential=os.environ.get("AppSecret"))

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def GetAccessTokenOnBehalfUser():
    idToken = get_token_auth_header()
    dic = app.acquire_token_on_behalf_of(user_assertion=idToken,
        scopes=["https://graph.microsoft.com/User.Read"])
    if "error" in dic.keys():
        return json.dumps(dic)
    else:
        return dic["access_token"]

def get_token_auth_header():
  """Obtains the Access Token from the Authorization Header
  """
  auth = request.headers.get("Authorization", None)
  if not auth:
      raise AuthError({"code": "authorization_header_missing",
                        "description":
                        "Authorization header is expected"}, 401)

  parts = auth.split()

  if parts[0].lower() != "bearer":
      raise AuthError({"code": "invalid_header",
                        "description":
                        "Authorization header must start with"
                        " Bearer"}, 401)
  elif len(parts) == 1:
      raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
  elif len(parts) > 2:
      raise AuthError({"code": "invalid_header",
                        "description":
                        "Authorization header must be"
                        " Bearer token"}, 401)

  token = parts[1]
  return token
