# 获取花椒直播的真实流媒体地址。

import requests
import time
from scripts.live.base import Base


class HuaJiao(Base):
    _name = '花椒'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid
        self.headers = {
            'Referer': 'https://h.huajiao.com/l/index?liveid={}&qd=hu'.format(rid)
        }

    def get_real_url(self):
        tt = str(time.time())
        try:
            room_url = 'https://h.huajiao.com/api/getFeedInfo?sid={tt}&liveid={rid}'.format(tt=tt, rid=self.rid)
            response = requests.get(url=room_url, headers=self.headers).json()
            real_url = response.get('data').get('live').get('main')
        except:
            return '直播间不存在或未开播'
        return real_url


if __name__ == '__main__':
    r = input('请输入花椒直播房间号：\n')
    print(HuaJiao(r).get_real_url())
