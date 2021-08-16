# 艾米直播：https://www.imifun.com/

import re

import requests

from scripts.live.base import Base


class IMFun(Base):
    _name = '艾米'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            res = s.get('https://www.imifun.com/' + str(self.rid)).text
        roomid = re.search(r"roomId:\s'([\w-]+)'", res)
        if roomid:
            status = re.search(r"isLive:(\d),", res).group(1)
            if status == '1':
                real_url = 'https://wsmd.happyia.com/ivp/{}.flv'.format(roomid.group(1))
                return real_url
            else:
                return '未开播'
        else:
            return '直播间不存在'


if __name__ == '__main__':
    r = input('输入艾米直播房间号：\n')
    print(IMFun(r).get_real_url())
