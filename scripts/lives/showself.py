# 秀色直播：https://www.showself.com/

from urllib.parse import urlencode
import requests
import time
import hashlib
from scripts.base import Base


class ShowSelf(Base):
    _name = '秀色'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        with requests.Session() as s:
            res = s.get('https://service.showself.com/v2/custuser/visitor').json()
        uid = res['data']['uid']
        accesstoken = sessionid = res['data']['sessionid']
        params = {
            'accessToken': accesstoken,
            'tku': uid,
            '_st1': int(time.time() * 1000)
        }
        payload = {
            'groupid': '999',
            'roomid': self.rid,
            'sessionid': sessionid,
            'sessionId': sessionid
        }
        data = dict(params, **payload)
        data = urlencode(sorted(data.items(), key=lambda d: d[0])) + 'sh0wselfh5'
        _ajaxData1 = hashlib.md5(data.encode('utf-8')).hexdigest()
        payload['_ajaxData1'] = _ajaxData1
        url = 'https://service.showself.com/v2/rooms/{}/members?{}'.format(self.rid, urlencode(params))
        with requests.Session() as s:
            res = s.post(url, json=payload)
        if res.status_code == 200:
            res = res.json()
            statuscode = res['status']['statuscode']
            if statuscode == '0':
                if res['data']['roomInfo']['live_status'] == '1':
                    anchor, = res['data']['roomInfo']['anchor']
                    real_url = anchor['media_url']
                    return real_url
                else:
                    return '未开播'
            else:
                return '房间不存在'
        else:
            return '参数错误'


if __name__ == '__main__':
    rid = input('输入秀色直播房间号：\n')
    print(ShowSelf(rid).get_real_url())
