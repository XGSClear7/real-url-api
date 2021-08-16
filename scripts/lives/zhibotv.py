# -*- coding: utf-8 -*-
# @Time: 2021/5/13 20:27
# @Project: real-url
# @Author: wbt5
# @Blog: https://wbt5.com

import requests

from scripts.base import Base


class ZhiBotv(Base):
    _name = '中国体育'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid
        self.params = {

            'token': '',
            'roomId': self.rid,
            'angleId': '',
            'lineId': '',
            'definition': 'hd',
            'statistics': 'pc|web|1.0.0|0|0|0|local|5.0.1',

        }

    def get_real_url(self):
        """
        no streaming 没开播;
        non-existent rid 房间号不存在;
        :return: url
        """
        with requests.Session() as s:
            res = s.get('https://rest.zhibo.tv/room/get-pull-stream-info-v430', params=self.params).json()
            if 'hlsHUrl' in res['data']:
                url = res['data'].get('hlsHUrl')
                if url:
                    return url
                else:
                    return 'no streaming'
            else:
                return 'non-existent rid'


if __name__ == '__main__':
    r = input('请输入中国体育房间号：\n')
    print(ZhiBotv(r).get_real_url())
