import json
import requests
import urllib.parse
from src.base.constants import *
from json import JSONDecodeError
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger


class HttpUtils:

    @staticmethod
    @auto_logger(logger)
    def get_authorization_token():
        data = {
            'client_id': 'developers-local-backend',
            'grant_type': 'password',
            'username': BaseConfig.USERNAME,
            'password': BaseConfig.PASSWORD,
            'client_secret': BaseConfig.CLIENT_SECRET
        }
        encoded_data = urllib.parse.urlencode(data)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        try:
            _response = requests.post(BaseConfig.TOKEN_URL, data=encoded_data, headers=headers)
            try:
                body = json.loads(_response.text)
                tkn = body['access_token']
            except JSONDecodeError as er:
                logger.error(F"{er.__class__.__name__} failed to parse json response, please check request.")
                raise er
            logger.info(AUTHORIZATION.format(tkn))
            return tkn
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} get_authorization_token failed with error: {e}")
            raise e

