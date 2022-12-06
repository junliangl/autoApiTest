import yaml
from common.common_object.common_object import YAML_PATH


class Yaml:
    __single = None

    def __new__(cls, *args, **kwargs):
        if not cls.__single:
            cls.__single = super().__new__(cls)
        return cls.__single

    def __init__(self):
        self.file = YAML_PATH

    def get_api(self):
        with open(self.file, mode='r', encoding='utf-8') as o:
            data = yaml.safe_load(o)
            return data

    def get_sql(self):
        pass


if __name__ == '__main__':
    test = Yaml()
    test.get_api()
