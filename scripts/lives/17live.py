# 获取17直播的真实流媒体地址，可能需要挂国外代理才行。
# 17直播间链接形式：https://17.live/live/276480

import requests

from scripts.base import Base


class Live17(Base):
    _name = '17'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid
        # 可能需要挂代理。
        # self.proxies = {
        #     "http": "http://xxxx:1080",
        #     "https": "http://xxxx:1080",
        # }

    def get_real_url(self):
        try:
            response = requests.get(url='https://api-dsa.17app.co/api/v1/lives/' + self.rid).json()
            real_url_default = response.get('rtmpUrls')[0].get('url')
            real_url_modify = real_url_default.replace('global-pull-rtmp.17app.co', 'china-pull-rtmp-17.tigafocus.com')
            real_url = [real_url_modify, real_url_default]
        except:
            return '直播间不存在或未开播'
        return real_url


if __name__ == '__main__':
    r = input('请输入17直播房间号：\n')
    print(Live17(r).get_real_url())
