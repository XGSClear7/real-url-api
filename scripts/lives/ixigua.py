# 获取西瓜直播的真实流媒体地址。

import re

import requests

from scripts.base import Base


class IXiGua(Base):
    _name = '西瓜'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        try:
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:83.0) Gecko/20100101 Firefox/83.0'
            }
            room_url = 'https://live.ixigua.com/' + str(self.rid)
            response = requests.get(url=room_url, headers=headers).text
            real_url = re.findall(r'playInfo":([\s\S]*?),"authStatus', response)[0]
            real_url = re.sub(r'\\u002F', '/', real_url)
        except:
            return '直播间不存在或未开播'
        return real_url


if __name__ == '__main__':
    r = input('请输入西瓜直播房间号：\n')
    print(IXiGua(r).get_real_url())
