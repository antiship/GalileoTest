from config import BaseConfig
from src.base.utils.http_utils import HttpUtils


class BaseService:
    def __init__(self):
        self.net_url = "https://" + BaseConfig.BASE_URL
        self.tkn = HttpUtils.get_authorization_token()
        self.net_headers = {
            "Authorization": "Bearer " + self.tkn,
            "Connection": "keep-alive",
            "Host": BaseConfig.BASE_URL,
            "Accept": "*/*",
            "authority": "pm.galileosky.com",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU, ru; q=0.9, en-US; q=0.8, en; q=0.7",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/118.0.0.0 Safari/537.36"
        }
        self.sw_url = "http://" + BaseConfig.SWAGGER_URL
        self.sw_headers = {
            'Accept': 'application/json'
        }
