import requests
from src.base.auto_logger import auto_logger, logger
from src.base.constants import SVC_RESPONSE
from src.base.net.base_svc import BaseService


class ServiceService(BaseService):
    @auto_logger(logger)
    def get_health(self):
        uri = self.sw_url + "/healthz"
        try:
            _response = requests.request("GET", uri, headers=self.sw_headers, allow_redirects=True)
            return _response, _response.reason
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} get_health failed with error: {e}")
            raise e

    @auto_logger(logger)
    def get_metrics(self):
        uri = self.sw_url + "/metrics"
        try:
            _response = requests.request("GET", uri, headers=self.sw_headers, allow_redirects=True)
            body = str(_response.text)
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} get_metrics failed with error: {e}")
            raise e
