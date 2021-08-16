# 获取战旗直播（战旗TV）的真实流媒体地址。https://www.zhanqi.tv/lives
# 默认最高画质

import json

import requests

from scripts.base import Base


class ZhanQi(Base):
    _name = '战旗'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid
        self.s = requests.Session()

    def get_real_url(self):

        res = self.s.get('https://m.zhanqi.tv/api/static/v2.1/room/domain/{}.json'.format(self.rid))
        try:
            res = res.json()
            videoid = res['data']['videoId']
            status = res['data']['status']
        except (KeyError, json.decoder.JSONDecodeError):
            return 'Incorrect rid'

        if status == '4':
            # 获取gid
            res = self.s.get('https://www.zhanqi.tv/api/public/room.viewer')
            try:
                res = res.json()
                gid = res['data']['gid']
            except KeyError:
                return 'Getting gid incorrectly'

            # 获取cdn_host
            res = self.s.get('https://umc.danuoyi.alicdn.com/dns_resolve_https?app=zqlive&host_key=alhdl-cdn.zhanqi.tv')
            cdn_host, *_ = res.json().get('redirect_domain')

            # 获取chain_key
            data = {
                'stream': f'{videoid}.flv',
                'cdnKey': 202,
                'platform': 128,
            }
            headers = {
                'cookie': f'gid={gid}',
            }
            res = self.s.post('https://www.zhanqi.tv/api/public/burglar/chain', data=data, headers=headers).json()
            chain_key = res['data']['key']
            url = f'https://{cdn_host}/alhdl-cdn.zhanqi.tv/zqlive/{videoid}.flv?{chain_key}&playNum=68072487067' \
                  f'&gId={gid}&ipFrom=1&clientIp=&fhost=h5&platform=128 '

            return url
        else:
            return 'No streaming'


if __name__ == '__main__':
    r = input('输入战旗直播房间号：\n')
    print(ZhanQi(r).get_real_url())
