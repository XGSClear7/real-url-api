# 获取映客直播的真实流媒体地址。

import requests

from scripts.base import Base


class InKe(Base):
    _name = '映客'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        try:
            room_url = 'https://webapi.busi.inke.cn/web/live_share_pc?uid=' + str(self.rid)
            response = requests.get(url=room_url).json()
            record_url = response.get('data').get('file').get('record_url')
            stream_addr = response.get('data').get('live_addr')
            real_url = {
                'record_url': record_url,
                'stream_addr': stream_addr
            }
        except:
            return '直播间不存在或未开播'
        return real_url


if __name__ == '__main__':
    r = input('请输入映客直播房间号：\n')
    print(InKe(r).get_real_url())
