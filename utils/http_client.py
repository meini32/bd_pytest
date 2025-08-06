import requests

class HttpClient:
    """简单封装 requests GET 请求"""

    @staticmethod
    def get(url, headers=None, params=None):
        response = requests.get(url, headers=headers, params=params)
        return response
