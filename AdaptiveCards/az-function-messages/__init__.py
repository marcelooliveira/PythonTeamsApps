from flask import Flask,request,Response
import azure.functions as func 
import os
import json
import sys
import traceback
from datetime import datetime

from botbuilder.schema import Activity, ActivityTypes
from botbuilder.core import(  
    BotFrameworkAdapterSettings,
    BotFrameworkAdapter,  
    TurnContext
)

import asyncio
# from Bots.activitybot import ActivityBot
from http import HTTPStatus
from aiohttp.web import Request, Response, json_response
from bots.teams_task_module_bot import TeamsTaskModuleBot
from config import DefaultConfig

CONFIG = DefaultConfig()

app = Flask(__name__)

botadaptersettings = BotFrameworkAdapterSettings("","")
botadapter = BotFrameworkAdapter(botadaptersettings)

SETTINGS = BotFrameworkAdapterSettings(os.environ.get("MicrosoftAppId"), os.environ.get("MicrosoftAppPassword"))
ADAPTER = BotFrameworkAdapter(SETTINGS)

BOT = TeamsTaskModuleBot(CONFIG)

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(app).handle(req, context)

@app.route("/api/az-function-messages",methods=["POST"])
async def messages():
    if "application/json" in request.headers["content-type"]:
        jsonmessage = request.json
    else:
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    activity = Activity().deserialize(jsonmessage)

    auth_header = request.headers["Authorization"] if "Authorization" in request.headers else ""

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return response.body["content"]["body"]
    return func.HttpResponse(status_code=HTTPStatus.OK)
