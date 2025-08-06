import pytest
import json
import os
from datetime import datetime

# ---- pytest HTML 报告 hook ----
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

# ---- session 级 fixture：加载测试数据 ----
@pytest.fixture(scope="session")
def load_urls():
    file_path = os.path.join(os.path.dirname(__file__), "../data/urls.json")
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
    return data
