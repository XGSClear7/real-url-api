# 获取六间房直播的真实流媒体地址。

import re

import requests

from scripts.live.base import Base


class V6CN(Base):
    _name = '六间房'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        try:
            response = requests.get('https://v.6.cn/' + str(self.rid)).text
            result = re.findall(r'"flvtitle":"v(\d*?)-(\d*?)"', response)[0]
            uid = result[0]
            flvtitle = 'v{}-{}'.format(*result)
            response = requests.get('https://rio.6rooms.com/live/?s=' + str(uid)).text
            hip = 'https://' + re.findall(r'<watchip>(.*\.xiu123\.cn).*</watchip>', response)[0]
            real_url = [hip + '/' + flvtitle + '/playlist.m3u8', hip + '/httpflv/' + flvtitle]
        except:
            return '直播间不存在或未开播'
        return real_url


if __name__ == '__main__':
    r = input('请输入六间房直播房间号：\n')
    print(V6CN(r).get_real_url())
