# -*- coding: utf-8 -*-
# 日志模块
from loguru import logger

logger.add('./Logs/Runtime.log', level='DEBUG', retention='7 days')
logger.add('./Logs/OOCLError.log', level='ERROR', retention='7 days')

# api配置
API_HOST = '0.0.0.0'
API_PORT = 7000
API_THREADED = True
