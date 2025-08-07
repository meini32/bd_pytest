import requests

def test_get_baidu(baidu_data):
    url = baidu_data["url"]
    headers = baidu_data["headers"]

    response = requests.get(url, headers=headers)

    print("状态码:", response.status_code)

    assert response.status_code == 200
