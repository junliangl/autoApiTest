import pymysql
from common.utils.get_config import Config_Info
from common.common_object.common_object import db_log


class UseDataBase:
    __single = None
    __db = Config_Info().get_db()

    def __new__(cls, *args, **kwargs):
        if not cls.__single:
            cls.__single = super().__new__(cls)
        return cls.__single

    def __init__(self):
        self.connect = pymysql.connect(host=self.__db[0],
                                       port=self.__db[1],
                                       user=self.__db[2],
                                       password=self.__db[3],
                                       db=self.__db[4])
        self.cursor = self.connect.cursor()

    def __str__(self):
        return "使用数据库, 包括 sql语句, 关闭数据库"

    def use_db(self, sql: str, data=None, *args, **kwargs):
        """
        操作数据库
        """
        self.cursor.execute(sql, data)
        result = self.cursor.fetchall()
        return result

    def close_db(self):
        self.cursor.close()
        self.connect.close()
