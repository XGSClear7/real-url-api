# 获取龙珠直播的真实流媒体地址，默认最高码率。

import re

import requests

from scripts.base import Base


class LongZhu(Base):
    _name = '龙珠'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        try:
            response = requests.get('http://star.longzhu.com/' + str(self.rid)).text
            roomId = re.findall(r'roomid":(\d+)', response)[0]
            response = requests.get(
                'http://livestream.longzhu.com/live/getlivePlayurl?roomId={}&utmSr=&platform=h5&device=ios'.format(
                    roomId)).json()
            real_url = response.get('playLines')[0].get('urls')[0].get('securityUrl')
        except:
            return '直播间不存在或未开播'
        return real_url


if __name__ == '__main__':
    r = input('请输入龙珠直播房间号：\n')
    print(LongZhu(r).get_real_url())
