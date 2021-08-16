# 乐嗨直播：https://www.lehaitv.com/

import hashlib
import time
from urllib.parse import unquote
from urllib.parse import urlencode

import requests

from scripts.live.base import Base


class LeHai(Base):
    _name = '乐嗨'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        url = 'https://service.lehaitv.com/v2/room/{}/enter'.format(self.rid)
        params = {
            '_st1': int(time.time() * 1e3),
            'accessToken': 's7FUbTJ%2BjILrR7kicJUg8qr025ZVjd07DAnUQd8c7g%2Fo4OH9pdSX6w%3D%3D',
            'tku': 3000006,
        }
        data = urlencode(params) + '1eha12h5'
        _ajaxData1 = hashlib.md5(data.encode('utf-8')).hexdigest()
        params['_ajaxData1'] = _ajaxData1
        params['accessToken'] = unquote(params['accessToken'])
        with requests.Session() as s:
            res = s.get(url, params=params)
        if res.status_code == 200:
            res = res.json()
            statuscode = res['status']['statuscode']
            if statuscode == '0':
                if res['data']['live_status'] == '1':
                    anchor, = res['data']['anchor']
                    real_url = anchor['media_url']
                    return real_url
                else:
                    return '未开播'
            else:
                return '房间不存在 或 权限检查错误'
        else:
            return '请求错误'


if __name__ == '__main__':
    r = input('输入乐嗨直播房间号：\n')
    print(LeHai(r).get_real_url())
