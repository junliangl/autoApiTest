import requests
import os
import json
from framework.logger import Logger

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(project_path)
logger = Logger("API测试流程").get_log()


class BaseApi:

    def __init__(self, session):
        self.session: requests.Session() = session

    def __str__(self):
        return ""

    def get(self, url):
        """
        GET 请求的封装方法
        :param url: str 格式的 url 链接
        :return:返回 session.get()对象
        """
        logger.info(f"发送 get 请求到:{url}")
        return self.session.get(url=url, verify=False)

    def post(self, url, data, headers):
        """
        POST 请求的封装方法
        :param url:str 格式的 url 链接
        :param json: json 格式请求体
        :param headers: json 格式的请求头
        :return:返回 session.post()对象
        """
        logger.info(f"发送 post 请求到{url}")
        return self.session.post(url=url, data=data, headers=headers, verify=False)

    def put(self, url, data, headers):
        """
        PUT 请求的封装方法
        :param url:str 格式的 url 链接
        :param json: json 格式请求体
        :param headers: json 格式的请求头
        :return:返回 session.post()对象
        """
        logger.info(f"发送 put 请求到{url}")
        return self.session.post(url=url, data=data, headers=headers)

    def delete(self, url):
        """
        DELETE 请求的封装方法
        :param url: str 格式的 url 链接
        :return:
        """
        logger.info(f"发送 delete 请求到{url}")
        return self.session.delete(url=url)

    @staticmethod
    def read_api_data(api_path_name, api_file_name):
        """
        读取 接口json 数据
        :param api_path_name: 对应每个接口上级目录路径
        :param api_file_name: 对应每个接口文件路径
        :return:
        """
        data_path = os.path.join(os.path.join(os.path.join(project_path, 'data'), api_path_name), api_file_name)
        with open(data_path, encoding='utf-8') as o:
            api_dict: dict = json.load(o)
        return api_dict

    @staticmethod
    def json_dumps(_dict):
        """
        把 dict 转换为 json 格式
        :param _dict: dict 数据
        :return: json 格式
        """
        return json.dumps(_dict)

    @staticmethod
    def json_loads(_json) -> dict:
        """
        把 json 转换为 dict 格式
        :param _json: json 数据
        :return: dict 数据
        """
        return json.loads(_json)
