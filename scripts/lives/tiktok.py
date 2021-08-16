# -*- coding: utf-8 -*-
# @Time: 2021/5/2 23:23
# @Project: real-url
# @Author: wbt5
# @Blog: https://wbt5.com

import re

import requests

from scripts.live.base import Base


class TikTok(Base):
    _name = 'TIKTOK'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        }
        res = requests.get(self.rid, headers=headers).text
        url = re.search(r'"LiveUrl":"(.*?m3u8)",', res)

        if url:
            return url.group(1)
        else:
            return 'link invalid'


if __name__ == '__main__':
    # https://vm.tiktok.com/ZMe45tomE
    r = input('请输入 TikTok 分享链接：\n')
    print(TikTok(r).get_real_url())
