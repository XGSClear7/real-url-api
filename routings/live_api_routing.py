# -*- coding: utf-8 -*-
from loguru import logger
from loguru import logger
from scripts import __all__ as scripts_cls


class RunScripts:

    def __init__(self, live_platform, parameter):
        self.scripts_cls = scripts_cls
        self.live_platform = live_platform
        self.parameter = parameter
        self.scripts = [scripts(self.parameter) for scripts in self.scripts_cls]

    @logger.catch
    def choice(self):
        """
        选择脚本
        :return:
        """
        for live_platform in self.scripts:
            if self.live_platform.upper() == live_platform._name:
                logger.info(f'live_platform {live_platform} to get live url.')
                data = live_platform.get_real_url()
                return data
        else:
            return


if __name__ == '__main__':
    print(RunScripts('羚萌', '24003').choice())
