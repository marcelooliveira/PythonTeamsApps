import azure.functions as func 
from flask import Flask
import sys
from cacheHelper import CacheHelper

app = Flask(__name__)

this = sys.modules[__name__]
this.cacheHelper = None

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    if this.cacheHelper is None:
        this.cacheHelper = CacheHelper(context.function_directory)
    return func.WsgiMiddleware(app).handle(req, context)

@app.route("/api/az-function-auth-end")
def index():
    return this.cacheHelper.render_cached_page(app, "auth_end.html")
