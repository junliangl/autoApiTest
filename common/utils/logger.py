# _*_ coding: utf-8 _*_
import logging
import os.path
import time
import colorlog


class Logger(object):
    log_colors_config = {
        'DEBUG': 'white',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red',
    }

    def __init__(self, description: str):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        """
        # 创建一个logger

        self.logger = logging.getLogger(description)
        self.logger.setLevel(logging.DEBUG)

        # 判断如果已经添加handler了就不需要添加
        if not self.logger.handlers:
            # 创建一个handler，用于写入日志文件
            rq = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
            root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            log_path = os.path.join(root_path, 'logs')
            log_name = os.path.join(log_path, rq + '.log')

            file_log = logging.FileHandler(log_name, encoding='utf-8')
            file_log.setLevel(logging.DEBUG)

            # 再创建一个handler，用于输出到控制台
            stream_log = logging.StreamHandler()
            stream_log.setLevel(logging.DEBUG)

            # 定义handler的输出格式
            self.formatter_stream = colorlog.ColoredFormatter(
                '%(log_color)s %(asctime)s - %(name)s - %(levelname)s - %(message)s'
                , log_colors=self.log_colors_config)
            self.formatter_file = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_log.setFormatter(self.formatter_file)
            stream_log.setFormatter(self.formatter_stream)

            # 给logger添加handler
            self.logger.addHandler(file_log)
            self.logger.addHandler(stream_log)

    def get_log(self):
        return self.logger
