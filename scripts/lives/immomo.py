import requests

from scripts.base import Base


class ImMoMo(Base):
    _name = '陌陌'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        url = 'https://web.immomo.com/webmomo/api/scene/profile/roominfos'
        data = {
            'stid': self.rid,
            'src': 'url'
        }

        with requests.Session() as s:
            s.get('https://web.immomo.com')
            res = s.post(url, data=data).json()

        ec = res.get('ec', 0)
        if ec != 200:
            return '请求参数错误'
        else:
            live = res['data']['live']
            if live:
                real_url = res['data']['url']
                return real_url
            else:
                return '未开播'


if __name__ == '__main__':
    r = input('请输入陌陌直播房间号：\n')
    print(ImMoMo(r).get_real_url())
