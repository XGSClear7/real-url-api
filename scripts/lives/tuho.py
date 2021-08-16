# 星光直播：https://www.tuho.tv/28545037

import re

import requests

from scripts.live.base import Base


class TuHo(Base):
    _name = '星光'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            res = s.get('https://www.tuho.tv/' + str(self.rid)).text
        flv = re.search(r'videoPlayFlv":"(https[\s\S]+?flv)', res)
        if flv:
            status = re.search(r'isPlaying\s:\s(\w+),', res).group(1)
            if status == 'true':
                real_url = flv.group(1).replace('\\', '')
                return real_url
            else:
                return '未开播'
        else:
            return '直播间不存在'


if __name__ == '__main__':
    r = input('输入星光直播房间号：\n')
    print(TuHo(r).get_real_url())
