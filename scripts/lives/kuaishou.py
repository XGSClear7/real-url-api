# 获取快手直播的真实流媒体地址，默认输出最高画质
# https://live.kuaishou.com/u/KPL704668133
# 如获取失败，尝试修改 cookie 中的 did

import json
import re

import requests

from scripts.base import Base


class KuaiShou(Base):
    _name = '快手'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 '
                          '(KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'cookie': 'did=web_d563dca728d28b00336877723e0359ed'}
        with requests.Session() as s:
            res = s.get('https://m.gifshow.com/fw/live/{}'.format(self.rid), headers=headers)
            livestream = re.search(r'liveStream":(.*),"obfuseData', res.text)
            if livestream:
                livestream = json.loads(livestream.group(1))
                *_, hlsplayurls = livestream['multiResolutionHlsPlayUrls']
                urls, = hlsplayurls['urls']
                url = urls['url']
                return url
            else:
                return '直播间不存在或未开播'


if __name__ == '__main__':
    # KPL704668133
    r = input('请输入快手直播房间ID：\n')
    print(KuaiShou(r).get_real_url())
