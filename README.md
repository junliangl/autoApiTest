# Requests Api 自动化测试框架（基于 python 3）
## 框架目录构造： ##


- **[config]()**： 用来存储配置文件

- **[data]()**：可以存储接口数据和存储 ddt 数据驱动的账号数据文件

- **[framework]()**：框架底层封装层，可以根据自己的想法封装底层方法
  - *[logger.py]()*：封装了日志输入，包括文件输出和控制台的输出
  - *[base_api]()*：封装了 requests 库中常用的方法，包括 get post put delete 等

- **[logs]()**：用于接收日志文件的输出 

- **[page_objects]()**：用于完成对业务模块的实际实现

- **[Python_HTMLTestReportCN]()**：生成自动化测试报告网页html

- **[test_report]()**：用于接收测试报告文件的输出

- **[test_suites]()**：用于测试用例的存放和用例集合套件

- **[tools]()**：用于存放 requirements.txt文件和一些工具插件

