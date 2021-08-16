# 羚萌直播：https://live.51lm.tv/programs/Hot

from urllib.parse import urlencode
import requests
import time
import hashlib
from scripts.base import Base


class LM(Base):

    _name = '羚萌'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        roominfo = {'programId': self.rid}

        def g(d):
            return hashlib.md5((d + '#' + urlencode(roominfo) + '#Ogvbm2ZiKE').encode('utf-8')).hexdigest()

        lminfo = {
            'h': int(time.time()) * 1000,
            'i': -246397986,
            'o': 'iphone',
            's': 'G_c17a64eff3f144a1a48d9f02e8d981c2',
            't': 'H',
            'v': '4.20.43',
            'w': 'a710244508d3cc14f50d24e9fecc496a'
        }
        u = g(urlencode(lminfo))
        lminfo = 'G=' + u + '&' + urlencode(lminfo)
        with requests.Session() as s:
            res = s.post('https://www.51lm.tv/live/room/info/basic', json=roominfo, headers={'lminfo': lminfo}).json()
        code = res['code']
        if code == 200:
            status = res['data']['isLiving']
            if status == 'True':
                real_url = res['data']['playUrl']
                return real_url
            else:
                return '未开播'
        elif code == -1:
            return '输入错误'
        elif code == 1201:
            return '直播间不存在'


if __name__ == '__main__':
    r = input('输入羚萌直播房间号：\n')
    print(LM(r).get_real_url())
