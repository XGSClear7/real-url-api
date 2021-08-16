# 获取NOW直播的真实流媒体地址。

import requests

from scripts.live.base import Base


class Now(Base):
    _name = 'NOW'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        try:
            room_url = 'https://now.qq.com/cgi-bin/now/web/room/get_live_room_url?room_id={}&platform=8'.format(
                self.rid)
            response = requests.get(url=room_url).json()
            result = response.get('result')
            real_url = {
                'raw_hls_url': result.get('raw_hls_url', 0),
                'raw_rtmp_url': result.get('raw_rtmp_url', 0),
                'raw_flv_url': result.get('raw_flv_url', 0)
            }
        except:
            return '直播间不存在或未开播'
        return real_url


if __name__ == '__main__':
    r = input('请输入NOW直播间号：\n')
    print(Now(r))
