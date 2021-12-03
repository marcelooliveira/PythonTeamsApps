# from flask import Flask,request,Response
# import azure.functions as func 
# import os
# import sys
# from botbuilder.schema import Activity
# from botbuilder.core import(  
#     BotFrameworkAdapterSettings,
#     BotFrameworkAdapter,  
#     TurnContext
# )
# import asyncio
# from Bots.echobot import EchoBot
# from Bots.activitybot import ActivityBot
# from http import HTTPStatus
# from aiohttp.web import Request, Response, json_response

# app = Flask(__name__)

# loop = asyncio.get_event_loop()

# botadaptersettings = BotFrameworkAdapterSettings("","")
# botadapter = BotFrameworkAdapter(botadaptersettings)

# SETTINGS = BotFrameworkAdapterSettings(os.environ.get("MicrosoftAppId"), os.environ.get("MicrosoftAppPassword"))
# ADAPTER = BotFrameworkAdapter(SETTINGS)

# # bot = EchoBot()
# bot = ActivityBot(os.environ.get("ConnectionName"), os.environ.get("ApplicationBaseUrl"))

# def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
#     return func.WsgiMiddleware(app).handle(req, context)

# @app.route("/api/az-function-messages",methods=["POST"])
# async def messages():
#   if "application/json" in request.headers["content-type"]:
#       jsonmessage = request.json
#   else:
#       return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

#   activity = Activity().deserialize(jsonmessage)

#   auth_header = request.headers["Authorization"] if "Authorization" in request.headers else ""

#   try:
#     await ADAPTER.process_activity(activity, auth_header, bot.on_turn)
#   except Exception as e:
#     print(e)

# #   response = await ADAPTER.process_activity(activity, auth_header, bot.on_turn)
# #   if response:
# #       return json_response(data=response.body, status=response.status)
#   return ""

