import json
from json import JSONDecodeError
import requests
from src.base.auto_logger import auto_logger, logger
from src.base.constants import SVC_RESPONSE
from src.base.net.base_svc import BaseService


class WorkspaceEntityService(BaseService):
    @auto_logger(logger)
    def get_workspace_entities(self, workspace_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/entities"
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
            logger.exception(F"{e.__class__.__name__} get_workspace_entities failed with error: {e}")
            raise e

    @auto_logger(logger)
    def post_workspace_entity(self, device, workspace_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/entities"
        try:
            _response = requests.request("POST", uri, data=device, headers=self.sw_headers, allow_redirects=True)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as er:
                logger.error(F"{er.__class__.__name__} failed to parse json response: {er}")
                raise er
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} post_workspace_entity failed with error: {e}")
            raise e

    @auto_logger(logger)
    def delete_workspace_entity(self, workspace_pk, entity_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/entities/" + entity_pk
        try:
            _response = requests.request("DELETE", uri, headers=self.sw_headers, allow_redirects=True)
            body = str(_response.reason)
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} delete_workspace_entity failed with error: {e}")
            raise e

    @auto_logger(logger)
    def get_workspace_entity(self, workspace_pk, entity_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/entities/" + entity_pk
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
            logger.exception(F"{e.__class__.__name__} get_workspace_entity failed with error: {e}")
            raise e

    @auto_logger(logger)
    def update_workspace_entity(self, device, workspace_pk, entity_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/entities/" + entity_pk
        try:
            _response = requests.request("PUT", uri, data=device, headers=self.sw_headers, allow_redirects=True)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as er:
                logger.error(F"{er.__class__.__name__} failed to parse json response: {er}")
                raise er
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} update_workspace_entity failed with error: {e}")
            raise e
