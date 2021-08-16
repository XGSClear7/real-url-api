# 酷我聚星直播：http://jx.kuwo.cn/

import requests

from scripts.live.base import Base


class KuWo(Base):
    _name = '酷我聚星'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            res = s.get(
                'https://zhiboserver.kuwo.cn/proxy.p?src=h5&cmd=enterroom&rid={}&videotype=1&auto=1'.format(self.rid))
        res = res.json()
        try:
            livestatus = res['room']['livestatus']
        except KeyError:
            return '房间号错误'
        if livestatus == 2:
            real_url = res['live']['url']
            return real_url
        else:
            return '未开播'


if __name__ == '__main__':
    r = input('输入酷我聚星直播房间号：\n')
    print(KuWo(r).get_real_url())
