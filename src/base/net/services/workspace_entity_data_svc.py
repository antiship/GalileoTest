import json
from json import JSONDecodeError
import requests
from src.base.auto_logger import auto_logger, logger
from src.base.constants import SVC_RESPONSE
from src.base.net.base_svc import BaseService


class WorkspaceEntityDataService(BaseService):
    @auto_logger(logger)
    def get_workspace_entities_data(self, device_id, time_stamp, fields, workspace_pk="50", pagination=(0, 1000000)):
        querystring = {"DeviceID": device_id, "DateTime[gt]": time_stamp, "fields": fields, "sort": "DateTime",
                       "offset": pagination[0], "limit": pagination[1]}
        uri = self.net_url + "/workspaces/" + workspace_pk + "/entities/data?"
        try:
            _response = requests.request("GET", uri, headers=self.net_headers, params=querystring,
                                         allow_redirects=True, stream=True)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as er:
                logger.error(F"{er.__class__.__name__} failed to parse json response: {er}")
                raise er
            logger.info(SVC_RESPONSE.format(_response.reason))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} get_entities_data failed with error: {e}")
            raise e