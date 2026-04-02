import json
from json import JSONDecodeError
import requests
from src.base.auto_logger import auto_logger, logger
from src.base.constants import SVC_RESPONSE
from src.base.net.base_svc import BaseService


class UserService(BaseService):
    @auto_logger(logger)
    def get_user_profile(self):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/users/profile"
        try:
            _response = requests.request("GET", uri, headers=self.sw_headers, allow_redirects=True)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as er:
                logger.error(F"{er.__class__.__name__} failed to parse json response: {er}")
                raise er
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} get_user_profile failed with error: {e}")
            raise e
