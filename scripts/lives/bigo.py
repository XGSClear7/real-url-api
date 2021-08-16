# -*- coding: utf-8 -*-
# @Time: 2021/8/15 16:00
# @Project: my-spiders
# @Author: wbt5
# @Blog: https://wbt5.com

import requests

from scripts.live.base import Base


class bigo(Base):
    _name = 'bigo'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            url = f'https://ta.bigo.tv/official_website/studio/getInternalStudioInfo'
            res = s.post(url, data={'siteId': self.rid}).json()
            hls_src = res['data']['hls_src']
            play_url = hls_src if hls_src else '不存在或未开播'
            return play_url


if __name__ == '__main__':
    r = input('输入bigo直播房间号：\n')
    print(bigo(r).get_real_url())
