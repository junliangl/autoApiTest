# Requests Api 自动化测试框架（基于 python 3）
## 框架目录构造： ##


- **[config](./config)**： 用来存储配置文件

- **[data](./data)**：可以存储接口数据和存储 xlsx 数据驱动文档

- **[common](./common)**：框架底层封装层，可以根据自己的想法封装底层方法
  - *[common_object](./common/common_object)*: 存放公用的数据, 包括路径, 日志对象, 请求会话对象
    [实现文件](./common/common_object/common_object.py)
  - *[utils](./common/utils)*：存放各种工具模块, 包括 [日志](./common/utils/logger.py), 
    [数据库连接](./common/utils/db_connect.py), [读取配置文件](./common/utils/get_config.py),
    [读取 yaml 文件](./common/utils/get_yaml_data.py) 等等
  - *[base_api](./common/base_api.py)*：封装了 requests 库中常用的方法，包括 get post put delete 等

- **[logs](./logs)**：用于接收日志文件的输出 

- **[cases](./cases)**：用于完成对某一具体接口业务模块的实际实现

- **[Python_HTMLTestReportCN](./Python_HTMLTestReportCN)**：生成自动化测试报告网页html

- **[test_report](./test_report)**：用于接收测试报告文件的输出

- **[test_suites](./test_suites)**：用于测试用例的存放和用例集合套件

