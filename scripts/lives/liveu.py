# -*- coding: utf-8 -*-
# @Time: 2021/8/15 14:09
# @Project: my-spiders
# @Author: wbt5
# @Blog: https://wbt5.com

import requests

from scripts.live.base import Base


class liveU(Base):
    _name = 'liveu'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            url = f'https://mobile.liveu.me/appgw/v2/watchstartweb?sessionid=&vid={self.rid}'
            res = s.get(url).json()
            play_url = res['retinfo']['play_url'] if res['retval'] == 'ok' else '不存在或未开播'
            return play_url


if __name__ == '__main__':
    r = input('输入liveU直播房间号：\n')
    print(liveU(r).get_real_url())
