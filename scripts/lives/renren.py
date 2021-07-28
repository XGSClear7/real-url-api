# 人人直播：http://zhibo.renren.com/

import re

import requests

from scripts.base import Base


class RenRen(Base):
    _name = '人人'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            res = s.get('http://activity.renren.com/liveroom/' + str(self.rid))
        livestate = re.search(r'"liveState":(\d)', res.text)
        if livestate:
            try:
                s = re.search(r'"playUrl":"([\s\S]*?)"', res.text).group(1)
                if livestate.group(1) == '0':
                    return s
                elif livestate.group(1) == '1':
                    return '回放：' + s
            except IndexError:
                return '解析错误'
        else:
            return '直播间不存在'


if __name__ == '__main__':
    r = input('请输入人人直播房间号：\n')
    print(RenRen(r).get_real_url())
