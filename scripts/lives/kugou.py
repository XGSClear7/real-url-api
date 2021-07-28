# 获取酷狗繁星直播的真实流媒体地址，默认最高码率。

import requests

from scripts.base import Base


class KuGou(Base):
    _name = '快手'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        try:
            response1 = requests.get(
                'https://fx1.service.kugou.com/video/pc/live/pull/v3/streamaddr?roomId={}&ch=fx&version=1.0&streamType=1-2-5&platform=7&ua=fx-flash&kugouId=0&layout=1'.format(
                    self.rid)).json()
            response2 = requests.get(
                'https://fx1.service.kugou.com/video/mo/live/pull/h5/v3/streamaddr?roomId={}&platform=18&version=1000&streamType=3-6&liveType=1&ch=fx&ua=fx-mobile-h5&kugouId=0&layout=1'.format(
                    self.rid)).json()
            real_url_flv = response1.get('data').get('horizontal')[0].get('httpflv')[0]
            real_url_hls = response2.get('data').get('horizontal')[0].get('httpshls')[0]
        except:
            return '直播间不存在或未开播'
        return {"flv": real_url_flv, "hls": real_url_hls}


if __name__ == '__main__':
    r = input('请输入酷狗直播房间号：\n')
    print(KuGou(r).get_real_url())
