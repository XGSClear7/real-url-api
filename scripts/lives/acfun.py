# AcFun直播：https://live.acfun.cn/
# 默认最高画质

import json

import requests

from scripts.base import Base


class AcFun(Base):

    _name = 'ACFUN'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': '_did=H5_',
            'referer': 'https://m.acfun.cn/'
        }
        url = 'https://id.app.acfun.cn/rest/app/visitor/login'
        data = 'sid=acfun.api.visitor'
        with requests.Session() as s:
            res = s.post(url, data=data, headers=headers).json()
        userid = res['userId']
        visitor_st = res['acfun.api.visitor_st']

        url = 'https://api.kuaishouzt.com/rest/zt/live/web/startPlay'
        params = {
            'subBiz': 'mainApp',
            'kpn': 'ACFUN_APP',
            'kpf': 'PC_WEB',
            'userId': userid,
            'did': 'H5_',
            'acfun.api.visitor_st': visitor_st
        }
        data = 'authorId={}&pullStreamType=FLV'.format(self.rid)
        res = s.post(url, params=params, data=data, headers=headers).json()
        if res['result'] == 1:
            data = res['data']
            videoplayres = json.loads(data['videoPlayRes'])
            liveadaptivemanifest, = videoplayres['liveAdaptiveManifest']
            adaptationset = liveadaptivemanifest['adaptationSet']
            representation = adaptationset['representation'][-1]
            real_url = representation['url']
            return real_url
        else:
            return '直播已关闭'


if __name__ == '__main__':
    r = input('请输入AcFun直播房间号：\n')
    print(AcFun(r).get_real_url())
