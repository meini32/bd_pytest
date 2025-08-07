import pytest
import json
import os
from datetime import datetime


#	用来准备“测试数据”，可自动注入到测试函数中
@pytest.fixture(scope="session")
def baidu_data():
    """读取百度 GET 请求的测试数据"""
    file_path = os.path.join(os.path.dirname(__file__), "../data/baidu_data.json")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data


# --- hook: 测试开始前自动设置报告路径 ---
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    pytest 启动时运行的钩子函数，用于配置报告输出路径。
    每次运行自动生成带时间戳的 html 报告
    """
    # 报告保存路径
    report_dir = os.path.join(os.path.dirname(__file__), "../reports")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # 当前时间戳
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # 设置 HTML 报告路径（适用于 pytest-html 插件）
    config.option.htmlpath = os.path.join(report_dir, f"report_{now}.html")