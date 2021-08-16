# 企鹅体育：https://live.qq.com/directory/all

import requests
import re

from scripts.live.base import Base


class ESport(Base):
    _name = '企鹅体育'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            res = s.get('https://m.live.qq.com/' + str(self.rid))
        show_status = re.search(r'"show_status":"(\d)"', res.text)
        if show_status:
            if show_status.group(1) == '1':
                hls_url = re.search(r'"hls_url":"(.*)","use_p2p"', res.text).group(1)
                return hls_url
            else:
                return '未开播'
        else:
            return '直播间不存在'


if __name__ == '__main__':
    r = input('请输入企鹅体育直播房间号：\n')
    print(ESport(r).get_real_url())
