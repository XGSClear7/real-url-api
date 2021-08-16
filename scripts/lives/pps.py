# 获取PPS奇秀直播的真实流媒体地址。

import re
import time

import requests

from scripts.live.base import Base


class PPS(Base):
    _name = 'PPS奇秀'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        try:
            response = requests.get('http://m-x.pps.tv/room/' + str(self.rid)).text
            anchor_id = re.findall(r'anchor_id":(\d*),"online_uid', response)[0]
            tt = int(time.time() * 1000)
            url = 'http://m-x.pps.tv/api/stream/getH5?qd_tm={}&typeId=1&platform=7&vid=0&qd_vip=0&qd_uid={}&qd_ip=114.114.114.114&qd_vipres=0&qd_src=h5_xiu&qd_tvid=0&callback='.format(
                tt, anchor_id)
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'http://m-x.pps.tv/'
            }
            response = requests.get(url=url, headers=headers).text
            real_url = re.findall(r'"hls":"(.*)","rate_list', response)[0]
        except:
            return '直播间不存在或未开播'
        return real_url


if __name__ == '__main__':
    r = input('请输入奇秀直播房间号：\n')
    print(PPS(r).get_real_url())
