import logging

# 设置日志格式，包含行号信息
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - Line: %(lineno)d - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler("app.log"),
#         logging.StreamHandler()
#     ]
# )

# 使用配置文件初始化日志
import logging.config
import json

def setup_logging_from_file(config_file='logging.json'):
    with open(config_file, 'r') as f:
        config = json.load(f)
        logging.config.dictConfig(config)



setup_logging_from_file()

# 创建一个日志记录器
logger = logging.getLogger(__name__)

# 使用不同的日志级别记录信息
logger.debug("这是一个调试信息")
logger.info("这是一个普通信息")
logger.warning("这是一个警告信息")
logger.error("这是一个错误信息")
logger.critical("这是一个严重错误信息")

import module_a
module_a.function_a()

import module_b
module_b.function_b()

import module_c
module_c.function_c()
