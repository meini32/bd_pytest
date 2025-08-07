import pytest
import json
import os

@pytest.fixture(scope="session")
def baidu_data():
    """读取百度 GET 请求的测试数据"""
    file_path = os.path.join(os.path.dirname(__file__), "../data/baidu_data.json")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data
