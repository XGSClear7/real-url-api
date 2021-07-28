# 艺气山直播：http://www.173.com/room/category?categoryId=11

import requests

from scripts.base import Base


class YQS(Base):
    _name = '艺气山'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        params = 'roomId={}'.format(self.rid)
        with requests.Session() as s:
            res = s.post('http://www.173.com/room/getVieoUrl', params=params).json()
        data = res['data']
        if data:
            status = data['status']
            if status == 2:
                return data['url']
            else:
                return '未开播'
        else:
            return '直播间不存在'


if __name__ == '__main__':
    r = input('输入艺气山直播房间号：\n')
    print(YQS(r).get_real_url())
