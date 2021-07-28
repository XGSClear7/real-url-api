# 热猫直播：https://zhibo.yuanbobo.com/
import re

import requests

from scripts.base import Base


class YuanBoBo(Base):
    _name = '热猫'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            res = s.get('https://zhibo.yuanbobo.com/' + str(self.rid)).text
        stream_id = re.search(r"stream_id:\s+'(\d+)'", res)
        if stream_id:
            status = re.search(r"status:\s+'(\d)'", res).group(1)
            if status == '1':
                real_url = 'http://ks-hlslive.yuanbobo.com/live/{}/index.m3u8'.format(stream_id.group(1))
                return real_url
            else:
                return '未开播'
        else:
            return '直播间不存在'


if __name__ == '__main__':
    r = input('输入热猫直播房间号：\n')
    print(YuanBoBo(r).get_real_url())
