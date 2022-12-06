import time
import random
import requests
from common.utils.get_yaml_data import Yaml
from common.common_object.common_object import api_log, session


class BaseApi:
    __single = None

    def __new__(cls, *args, **kwargs):
        if not cls.__single:
            cls.__single = super().__new__(cls)
        return cls.__single

    def __init__(self):
        self.response = None
        self.data = Yaml()
        self.session: requests.Session() = session
        self.session.trust_env = False

    def __str__(self):
        return "封装了 requests 常用请求方式的 api 和一些静态常用方法"

    def request(self, **api_data):
        """
        :return: requests.Session().request()
        """
        self.response = self.session.request(**api_data)
        try:
            self.response = self.session.request(**api_data)
        except Exception as e:
            api_log.error("请求有问题, 请检查")
        finally:
            return self.response

    def get_cases_api(self, case):
        api_data = self.data.get_api()
        api_data[case].pop("response")
        return api_data[case]

    def get_response_api(self, case):
        response_data = self.data.get_api()
        response = response_data[case]["response"]
        return response

    def get_status_code(self):
        status_code = self.response.status_code
        api_log.info(f"响应结果状态码:{status_code}")
        return status_code

    def get_text(self):
        pass

    def get_json(self):
        pass

    def get_cookies(self):
        pass

    def set_encode(self):
        pass

    def get_authorization(self):
        pass

    def close_request(self):
        """
        关闭 request 的 session 会话
        :return:
        """
        self.session.close()
        api_log.info("关闭 session 回话成功")

    @staticmethod
    # 得到随机的一个名字
    def get_random_name():
        random_name = ''
        for i in range(5):
            random_name = random_name + random.choice('abcdefghijklmnopqrstuvwxyz')
        return 'test_' + random_name

    @staticmethod
    # 得到一个随机的代号
    def get_random_number():
        random_number = ''
        for i in range(4):
            random_number = random_number + str(random.randint(1, 9))
        return random_number

    @staticmethod
    def get_time():
        date_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        return date_time
