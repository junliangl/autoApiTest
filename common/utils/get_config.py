from configparser import ConfigParser
from common.common_object.common_object import CONFIG_PATH


class Config_Info:
    __single = None

    def __new__(cls, *args, **kwargs):
        if not cls.__single:
            cls.__single = super().__new__(cls)
        return cls.__single

    def __init__(self):
        # 其他的初始化参数
        self.another = None
        self.database = ["host", "port", "user", "password", "db"]
        self.read_config = ConfigParser()

    # 得到配置里的 db 数据
    def get_db(self, db_conf_name="DB_1"):
        temp = 0
        self.read_config.read(CONFIG_PATH)
        for i in range(5):
            self.database[i] = self.read_config.get(db_conf_name, self.database[i])
        for i in self.database:
            if i.isdigit():
                self.database[temp] = int(i)
            temp += 1
        return self.database

    # 得到其他的配置, 可以重写
    def get_another(self):
        pass
