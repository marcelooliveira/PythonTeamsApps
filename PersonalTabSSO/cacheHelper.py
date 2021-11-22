from flask import render_template
import os

class CacheHelper:
    function_directory = ''
    cache = dict()
    cacheDisabled = False
    def __init__(self, function_directory):
        self.cacheDisabled = (os.environ.get("CacheEnabled") == "false")
        self.function_directory = function_directory

    def get_file(self, file):
        base_path = os.path.dirname(f"{self.function_directory}function.json")
        file_path = f"{base_path}{file}"
        with open(file_path, 'r') as f:
            return f.read()

    def render_cached_page(self, app, template):
        if self.cacheDisabled or template not in self.cache:
            app.root_path = os.path.dirname(app.root_path)
            auth_js = self.get_file("/static/js/auth.js")
            self.cache[template] = render_template(template, context = { "AzureClientId": os.environ.get("ClientId"), "auth_js": auth_js })
        return self.cache[template]

