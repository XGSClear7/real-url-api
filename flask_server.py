# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api

from loguru import logger
from apps.live_url_api import live_api
from config import *

# 注册flask
app = Flask(__name__)
# restful
api = Api(app)
# encode
app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
app.config['JSON_AS_ASCII'] = False
# registered
app.register_blueprint(live_api, url_prefix='/live-api')

if __name__ == '__main__':
    logger.info(f"server run on {API_HOST}:{API_PORT}. threaded is {'on' if API_THREADED else 'off'}.")
    app.run(host=API_HOST, port=API_PORT, threaded=API_THREADED)