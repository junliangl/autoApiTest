import unittest
from cases.case1.demo1 import Demo1
from common.common_object.common_object import result_log


class TestDemo(unittest.TestCase):
    """
    测试demon模块 API
    """

    @classmethod
    def setUp(cls) -> None:
        cls.test = Demo1()

    @classmethod
    def tearDown(cls) -> None:
        pass

    def test1_demo(self):
        """
        测试 demo1
        """
        result = self.test.get_demo1_result()
        if result:
            self.assertTrue(result)
        else:
            self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
