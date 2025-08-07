# bd_pytest

## ✅ 项目目的

通过对百度页面的 GET 请求进行自动化测试，快速熟悉 `pytest` 测试框架的核心流程，包括：

- 项目结构分层
- 数据驱动（data）
- fixtures 自动传参
- 测试执行流程
- 报告生成

---

## 📁 项目结构说明

### 整体架构
划分层面：用例层tests、数据层data、配置文件、依赖性清单

project/
├── tests/
│   ├── test_api/          
│   │   └── test_baidu.py      ← 💡测试用例：这里写测试函数
│   └── conftest.py            ← 💡共享配置：定义 fixture，供其他测试文件使用
├── data/
│   └── baidu_data.json        ← 💡测试数据：用 JSON 管理请求头/参数
├── pytest.ini                 ← 💡配置文件：告诉 pytest 搜哪些文件、生成啥报告等
└── requirements.txt           ← 💡依赖清单：安装环境依赖




## 如何运行测试？
直接在终端输入 pytest回车即可生成报告
pytest -s --html=reports/report.html 带上详细输出和生成报告


## 学习疑问

#### Q1:这里为什么不需要main？哪里是程序的执行入口？
- ans：哈哈被你发现了pytest的奥秘啦
- 先说结论：执行 pytest 命令时，其实你运行的是 pytest 工具的“主函数”
- 它会根据配置文件 pytest.ini 指定的路径，自动扫描所有符合规则的测试文件
- 默认规则是：
文件名以 test_ 开头的 .py 文件
函数名以 test_ 开头
类名以 Test 开头（内部函数也要以 test_ 开头）

#### Q2:测试函数 def test_get_baidu(baidu_data) 的参数是从哪来的？
那它执行这个函数 的参数 怎么传进去的？
ans：来自 pytest 的 fixture 注入机制（又叫依赖注入）

你在 conftest.py 里定义了一个 @pytest.fixture 修饰的函数 baidu_data
pytest 在执行测试函数前，会自动查找是否有叫 baidu_data 的 fixture
找到了就执行 fixture，把返回值传进去
拿到返回值之后，自动作为参数传给测试函数