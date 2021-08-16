# KK直播：http://www.kktv5.com/
import requests

from scripts.live.base import Base


class KK(Base):
    _name = 'KK'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        url = 'https://sapi.kktv1.com/meShow/entrance?parameter={}'
        parameter = {'FuncTag': 10005043, 'userId': '{}'.format(self.rid), 'platform': 1, 'a': 1, 'c': 100101}
        with requests.Session() as s:
            res = s.get(url.format(parameter)).json()
        tagcode = res['TagCode']
        if tagcode == '00000000':
            if res.get('liveType', 0) == 1:
                roomid = res['roomId']
                parameter = {'FuncTag': 60001002, 'roomId': roomid, 'platform': 1, 'a': 1, 'c': 100101}
                with requests.Session() as s:
                    res = s.get(url.format(parameter)).json()
                real_url = res['liveStream']
                return real_url
            else:
                return '未开播'
        else:
            return '直播间不存在'


if __name__ == '__main__':
    r = input('输入KK直播房间号：\n')
    print(KK(r).get_real_url())
