import requests
# from bd_pytest.utils.logger import logger

def test_get_baidu(baidu_data):
    url = baidu_data["url"]
    headers = baidu_data["headers"]
    # logger.info(f"请求地址: {url}")
    # logger.info(f"请求头: {headers}")

    response = requests.get(url, headers=headers)

    print("状态码:", response.status_code)

    assert response.status_code == 200
