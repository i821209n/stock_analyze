import logging

logger = logging.getLogger(__name__)

def function_c():
    # 使用不同的日志级别记录信息
    logger.debug("这是 module_c 的调试信息")
    logger.info("这是 module_c 的普通信息")
    logger.warning("这是 module_c 的警告信息")
    logger.error("这是 module_c 的错误信息")
    logger.critical("这是 module_c 的严重错误信息")
