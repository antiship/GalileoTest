import json
from json import JSONDecodeError
import requests
from src.base.auto_logger import auto_logger, logger
from src.base.constants import SVC_RESPONSE
from src.base.net.base_svc import BaseService


class WorkspaceService(BaseService):
    @auto_logger(logger)
    def get_workspaces(self):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces"
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
            logger.exception(F"{e.__class__.__name__} get_workspaces failed with error: {e}")
            raise e

    @auto_logger(logger)
    def post_workspace(self, workspace):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces"
        try:
            _response = requests.request("POST", uri, data=workspace, headers=self.sw_headers, allow_redirects=True)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as er:
                logger.error(F"{er.__class__.__name__} failed to parse json response: {er}")
                raise er
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} post_workspace failed with error: {e}")
            raise e

    @auto_logger(logger)
    def get_workspace(self, workspace_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk
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
            logger.exception(F"{e.__class__.__name__} get_workspace failed with error: {e}")
            raise e

    @auto_logger(logger)
    def update_workspace(self, workspace, workspace_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk
        try:
            _response = requests.request("PUT", uri, data=workspace, headers=self.sw_headers, allow_redirects=True)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as er:
                logger.error(F"{er.__class__.__name__} failed to parse json response: {er}")
                raise er
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} update_workspace failed with error: {e}")
            raise e

    @auto_logger(logger)
    def get_workspace_permissions(self, workspace_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/permissions"
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
            logger.exception(F"{e.__class__.__name__} get_workspace_permissions failed with error: {e}")
            raise e

    @auto_logger(logger)
    def delete_workspace(self, workspace_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk
        try:
            _response = requests.request("DELETE", uri, headers=self.sw_headers, allow_redirects=True)
            body = str(_response.reason)
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} delete_workspace failed with error: {e}")
            raise e
