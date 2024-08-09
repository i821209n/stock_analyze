import logging

logger = logging.getLogger(__name__)

def function_b():
    # 使用不同的日志级别记录信息
    logger.debug("这是 module_b 的调试信息")
    logger.info("这是 module_b 的普通信息")
    logger.warning("这是 module_b 的警告信息")
    logger.error("这是 module_b 的错误信息")
    logger.critical("这是 module_b 的严重错误信息")
