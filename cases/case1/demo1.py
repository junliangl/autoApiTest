from common.base_api import BaseApi
from common.utils.db_connect import UseDataBase
from common.common_object.common_object import ROOT_PATH, api_log


class Demo1:
    __single = None

    def __new__(cls, *args, **kwargs):
        if not cls.__single:
            cls.__single = super().__new__(cls)
        return cls.__single

    def __init__(self):
        self.__case = "first_case"
        self.base_api = BaseApi()
        # self.db = UseDataBase()

    def __del__(self):
        # self.base_api.session.close()
        pass

    def get_demo1_result(self):
        """
        :return:bool
        """
        response = self.base_api.request(**self.base_api.get_cases_api(self.__case))
        if response.status_code == int(self.base_api.get_response_api(self.__case)["code"]):
            return True
        else:
            return False
