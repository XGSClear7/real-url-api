# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask_restful import Resource
from flask_restful import reqparse
from loguru import logger
from routings.live_api_routing import RunScripts

live_api = Blueprint('live_api', __name__)

# 响应模板
return_model = {'state': 0, 'data': None}


class LiveUrl(Resource):
    """
    直播流接口
    """

    def __init__(self):
        self.return_data = return_model
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('live_platform', type=str, required=True, help='直播平台')
        self.reqparse.add_argument('parameter', type=str, required=True, help='需要解析的内容')
        super(LiveUrl, self).__init__()

    def get(self):
        # 定义消息体
        return_data = self.return_data.copy()
        # 接收front参数
        args = self.reqparse.parse_args()
        live_platform = args.get('live_platform')
        parameter = args.get('parameter')
        logger.info(f"req: live_platform-{live_platform} parameter-{parameter}")
        live_url = RunScripts(live_platform, parameter).choice()
        logger.info(f"res: live_platform-{live_platform} parameter-{parameter} res-{live_url}")
        if not live_url:
            return return_data
        return_data['state'] = 1
        return_data['data'] = live_url
        return return_data


class LiveUrlDocs(Resource):
    """
    接口文档
    """
    def get(self):
        """
        获取接口文档
        :return:
        """
        return render_template('LiveUrlDocs.html')


live_api.add_url_rule(rule='/api-docs', view_func=LiveUrlDocs.as_view('api-docs'))
live_api.add_url_rule(rule='/get-url', view_func=LiveUrl.as_view('get-live-url'))
