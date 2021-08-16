# -*- coding: utf-8 -*-
# @Time: 2021/5/1 13:03
# @Project: real-url
# @Author: wbt5
# @Blog: https://wbt5.com

import json

import requests

from scripts.live.base import Base


class MAOER(Base):
    _name = '猫耳'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 '
        }
        url = 'https://fm.missevan.com/api/v2/live/{}'.format(self.rid)
        with requests.Session() as s:
            res = s.get(url, headers=headers).json()
        try:
            code = res['code']
            if code != 0:
                return res['info']
            else:
                channel = res['info']['room']['channel']
                return channel
        except json.decoder.JSONDecodeError:
            return '输入错误'


if __name__ == '__main__':
    r = input('请输入猫耳直播房间号：\n')
    print(MAOER(r).get_real_url())
