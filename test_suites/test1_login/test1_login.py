import unittest
import requests
from framework.logger import Logger
from page_object.login.login import Login

logger = Logger("测试结果").get_log()


class TestLogin(unittest.TestCase):
    """
    测试登录模块 API
    """

    @classmethod
    def setUp(cls) -> None:
        cls.session = requests.Session()

    @classmethod
    def tearDown(cls) -> None:
        cls.session.close()

    def test1_init_page_api(self):
        """
        测试 访问登录界面 api
        :return: None
        """
        login_page = Login(self.session)
        result = login_page.get_init_page_api_result()
        if result:
            self.assertTrue(result, logger.info("接口无误"))
        else:
            self.assertTrue(result, logger.error("该接口有问题"))

    def test2_login_api(self):
        """
        测试 登录接口的 api
        :return: None
        """
        login_page = Login(self.session)
        result = login_page.get_login_api_result()
        if result:
            self.assertTrue(result, logger.info("接口无误"))
        else:
            self.assertTrue(result, logger.error("该接口有问题"))


if __name__ == '__main__':
    unittest.main()
