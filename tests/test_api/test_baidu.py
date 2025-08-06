import pytest
from bd_pytest.utils.http_client import HttpClient
from bd_pytest.utils.logger import logger


def test_baidu_homepage(load_urls):
    """测试百度首页 GET 请求"""
    url = load_urls["baidu"]
    logger.info(f"开始测试百度 GET 请求：{url}")

    response = HttpClient.get(url)

    logger.info(f"响应状态码：{response.status_code}")
    logger.info(f"响应头：{response.headers}")

    # 断言
    assert response.status_code == 200
    assert "百度" in response.text
