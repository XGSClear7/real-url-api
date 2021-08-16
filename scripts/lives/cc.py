# 获取网易CC的真实流媒体地址。
# 默认为最高画质

import requests

from scripts.base import Base


class CC(Base):
    _name = '网易CC'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        room_url = 'https://api.cc.163.com/v1/activitylives/anchor/lives?anchor_ccid=' + str(self.rid)
        response = requests.get(url=room_url).json()
        data = response.get('data', 0)
        if data:
            channel_id = data.get('{}'.format(self.rid)).get('channel_id', 0)
            if channel_id:
                response = requests.get('https://cc.163.com/live/channel/?channelids=' + str(channel_id)).json()
                real_url = response.get('data')[0].get('sharefile')
            else:
                return '直播间不存在'
        else:
            return '输入错误'
        return real_url


if __name__ == '__main__':
    r = input('请输入网易CC直播房间号：\n')
    print(CC(r).get_real_url())
