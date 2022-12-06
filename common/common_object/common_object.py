import os
import requests
from common.utils.logger import Logger

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_PATH = os.path.join(os.path.join(ROOT_PATH, 'config'), 'config.ini')
YAML_PATH = os.path.join(os.path.join(ROOT_PATH, 'data'), 'api.yml')
CSV_PATH = os.path.join(os.path.join(ROOT_PATH, 'data'), 'test.xlsx')


db_log = Logger(description="database测试流程").get_log()

api_log = Logger(description="API测试流程").get_log()

config_log = Logger(description="读取数据").get_log()

result_log = Logger(description="测试结果").get_log()

session = requests.Session()
