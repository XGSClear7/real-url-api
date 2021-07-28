# 获取企鹅电竞的真实流媒体地址。
# 默认画质为超清

import requests
import re
from scripts.base import Base


class EGame(Base):

    _name = '企鹅电竞'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        room_url = 'https://share.egame.qq.com/cgi-bin/pgg_async_fcgi'
        post_data = {
            'param': '''{"0":{"module":"pgg_live_read_svr","method":"get_live_and_profile_info","param":{"anchor_id":'''
                     + str(self.rid) + ''',"layout_id":"hot","index":1,"other_uid":0}}}'''
        }
        try:
            response = requests.post(url=room_url, data=post_data).json()
            data = response.get('data', 0)
            if data:
                video_info = data.get('0').get(
                    'retBody').get('data').get('video_info')
                pid = video_info.get('pid', 0)
                if pid:
                    is_live = data.get('0').get(
                    'retBody').get('data').get('profile_info').get('is_live', 0)
                    if is_live:
                        play_url = video_info.get('stream_infos')[
                            0].get('play_url')
                        real_url = re.findall(r'([\w\W]+?)&uid=', play_url)[0]
                    else:
                        return '直播间未开播'
                else:
                    return '直播间未启用'
            else:
                return '直播间不存在'
        except:
            return '数据请求错误'
        return real_url


if __name__ == '__main__':
    r = input('请输入企鹅电竞房间号：\n')
    print(EGame(r).get_real_url())
