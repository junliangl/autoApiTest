import os
from framework.base_api import BaseApi
from framework.logger import Logger

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger = Logger("API测试流程").get_log()


class Login(BaseApi):

    def get_init_page_api_result(self):
        """
        该接口测试进入页面
        :return:bool
        """
        api_path_name = 'login'
        api_file_name = 'init.json'
        post_data = self.read_api_data(api_path_name, api_file_name)
        try:
            url = post_data["url"]
        except KeyError as e:
            logger.error(
                f"目录:{os.path.join(os.path.join(os.path.join(project_path, 'config'), api_path_name), api_file_name)}不存在 url 数据")
            return False
        try:
            response = self.get(url)
        except Exception as e:
            logger.error("请求失败!请查看以下原因")
            logger.error(e)
            return False
        if response.status_code == 200:
            return True
        else:
            logger.error(f"当前响应码:{response.status_code},不为200!")
            return False

    def get_login_api_result(self):
        """
        该方法测试登录接口
        :return: bool
        """
        api_path_name = 'login'
        api_file_name = 'login.json'
        post_data = self.read_api_data(api_path_name, api_file_name)
        try:
            url = post_data["url"]
        except KeyError as e:
            logger.error(
                f"目录:{os.path.join(os.path.join(os.path.join(project_path, 'config'), api_path_name), api_file_name)}不存在 url 数据")
            return False
        try:
            data = post_data["json"]
        except KeyError as e:
            logger.error(
                f"目录:{os.path.join(os.path.join(os.path.join(project_path, 'config'), api_path_name), api_file_name)}不存在 json 数据!")
            return False
        try:
            headers = post_data["headers"]
        except KeyError as e:
            logger.error(
                f"目录:{os.path.join(os.path.join(os.path.join(project_path, 'config'), api_path_name), api_file_name)}不存在 json 数据!")
            return False
        # noinspection PyBroadException
        try:
            response = self.post(url, data, headers)
        except Exception as e:
            logger.error("请求失败!请查看以下原因")
            logger.error(e)
            return False
        try:
            if response.json()['msg'] == '操作成功' and response.json()['code'] == 0:
                return True
            else:
                logger.error(f"响应结果有问题,消息体如下:{response.json()}")
                return False
        except KeyError as e:
            logger.error("消息体字段存在问题!")
            logger.error(e)
            return False
