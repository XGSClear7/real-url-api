# 获取虎牙直播的真实流媒体地址。
# 虎牙"一起看"频道的直播间可能会卡顿，尝试将返回地址 tx.hls.huya.com 中的 tx 改为 bd、migu-bd。

import json
import re

import requests

from scripts.live.base import Base


class HuYa(Base):
    _name = '虎牙'

    def __init__(self, rid):
        super(Base, self).__init__()
        self.rid = rid

    def get_real_url(self):
        try:
            room_url = 'https://m.huya.com/' + str(self.rid)
            header = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 '
                              '(KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36 '
            }
            response = requests.get(url=room_url, headers=header).text
            streamInfo = \
            json.loads(re.findall(r"<script> window.HNF_GLOBAL_INIT = (.*)</script>", response)[0])["roomInfo"][
                "tLiveInfo"]["tLiveStreamInfo"]["vStreamInfo"]["value"]
            if streamInfo == []:
                return '未开播或直播间不存在'
            real_url = {}
            for info in streamInfo:
                real_url[info["sCdnType"].lower() + "_flv"] = info["sFlvUrl"] + "/" + info["sStreamName"] + "." + info[
                    "sFlvUrlSuffix"] + "?" + info["sFlvAntiCode"]
                real_url[info["sCdnType"].lower() + "_hls"] = info["sHlsUrl"] + "/" + info["sStreamName"] + "." + info[
                    "sHlsUrlSuffix"] + "?" + info["sHlsAntiCode"]
        except Exception as e:
            return '未开播或直播间不存在'
        return real_url


if __name__ == '__main__':
    rid = input('输入虎牙直播房间号：\n')
    print(HuYa(rid).get_real_url())
