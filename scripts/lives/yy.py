# 获取YY直播的真实流媒体地址。https://www.yy.com/1349606469
# 默认获取最高画质

import json
import re

import requests

from scripts.live.base import Base


class YY(Base):
    _name = 'YY'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        headers = {
            'referer': 'http://wap.yy.com/mobileweb/{rid}'.format(rid=self.rid),
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko)'
                          ' Version/11.0 Mobile/15A372 Safari/604.1'
        }
        room_url = 'http://interface.yy.com/hls/new/get/{rid}/{rid}/1200?source=wapyy&callback='.format(rid=self.rid)
        with requests.Session() as s:
            res = s.get(room_url, headers=headers)
        if res.status_code == 200:
            data = json.loads(res.text[1:-1])
            if data.get('hls', 0):
                xa = data['audio']
                xv = data['video']
                xv = re.sub(r'_0_\d+_0', '_0_0_0', xv)
                url = 'https://interface.yy.com/hls/get/stream/15013/{}/15013/{}?source=h5player&type=m3u8'.format(xv,
                                                                                                                   xa)
                res = s.get(url).json()
                real_url = res['hls']
                return real_url
            else:
                return '未开播'
        else:
            return '直播间不存在'


if __name__ == '__main__':
    r = input('输入YY直播房间号：\n')
    print(YY(r).get_real_url())
