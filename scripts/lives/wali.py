# 小米直播：https://live.wali.com/fe

import requests

from scripts.live.base import Base


class WaLi(Base):
    _name = '小米'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        zuid = self.rid.split('_')[0]
        with requests.Session() as s:
            res = s.get('https://s.zb.mi.com/get_liveinfo?lid={}&zuid={}'.format(self.rid, zuid)).json()
        status = res['data']['status']
        if status == 1:
            flv = res['data']['video']['flv']
            return flv.replace('http', 'https')
        else:
            return '直播间不存在或未开播'


if __name__ == '__main__':
    r = input('请输入小米直播房间号：\n')
    print(WaLi(r).get_real_url())
