# 获取哔哩哔哩直播的真实流媒体地址，默认获取直播间提供的最高画质
# qn=150高清
# qn=250超清
# qn=400蓝光
# qn=10000原画
import re

import requests
from scripts.live.base import Base


class BiliBili(Base):

    _name = '哔哩哔哩'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        # 先获取直播状态和真实房间号
        r_url = 'https://api.live.bilibili.com/room/v1/Room/room_init?id={}'.format(self.rid)
        with requests.Session() as s:
            res = s.get(r_url).json()
        code = res['code']
        if code == 0:
            live_status = res['data']['live_status']
            if live_status == 1:
                room_id = res['data']['room_id']

                def u(pf):
                    f_url = 'https://api.live.bilibili.com/xlive/web-room/v1/playUrl/playUrl'
                    params = {
                        'cid': room_id,
                        'platform': pf,
                        'otype': 'json',
                        'quality': 0
                    }
                    resp = s.get(f_url, params=params).json()
                    try:
                        durl = resp['data']['durl']
                        real_url = durl[0]['url']
                        real_url = re.sub(r'live_(\d+)_(\d+)_\d+.m3u8', r'live_\1_\2.m3u8', real_url)
                        return real_url
                    except KeyError or IndexError:
                        return '获取失败'

                return u('h5')
            else:
                return '未开播'
        else:
            return '房间不存在'


if __name__ == '__main__':
    r = input('请输入bilibili直播房间号：\n')
    print(BiliBili(r).get_real_url())
