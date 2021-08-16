# 棉花糖直播：https://www.2cq.com/rank

import requests

from scripts.live.base import Base


class MHT(Base):

    _name = '棉花糖'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            res = s.get('https://www.2cq.com/proxy/room/room/info?roomId={}&appId=1004'.format(self.rid))
        res = res.json()
        if res['status'] == 1:
            result = res['result']
            if result['liveState'] == 1:
                real_url = result['pullUrl']
                return real_url
            else:
                return '未开播'
        else:
            return '直播间可能不存在'


if __name__ == '__main__':
    r = input('输入棉花糖直播房间号：\n')
    print(MHT(r).get_real_url())
