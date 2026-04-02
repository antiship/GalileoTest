import json
from json import JSONDecodeError
import requests
from src.base.auto_logger import auto_logger, logger
from src.base.constants import SVC_RESPONSE
from src.base.net.base_svc import BaseService


class WorkspaceRoleService(BaseService):
    @auto_logger(logger)
    def get_workspace_roles(self, workspace_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/roles"
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
            logger.exception(F"{e.__class__.__name__} get_workspace_roles failed with error: {e}")
            raise e

    @auto_logger(logger)
    def post_workspace_role(self, role, workspace_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/roles"
        try:
            _response = requests.request("POST", uri, data=role, headers=self.sw_headers, allow_redirects=True)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as er:
                logger.error(F"{er.__class__.__name__} failed to parse json response: {er}")
                raise er
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} post_workspace_role failed with error: {e}")
            raise e

    @auto_logger(logger)
    def delete_workspace_role(self, workspace_pk, role_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/roles/" + role_pk
        try:
            _response = requests.request("DELETE", uri, headers=self.sw_headers, allow_redirects=True)
            body = str(_response.reason)
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} delete_workspace_role failed with error: {e}")
            raise e

    @auto_logger(logger)
    def get_workspace_role(self, workspace_pk, role_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/roles/" + role_pk
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
            logger.exception(F"{e.__class__.__name__} get_workspace_role failed with error: {e}")
            raise e

    @auto_logger(logger)
    def update_workspace_role(self, role, workspace_pk, role_pk):
        self.sw_headers.update({"Authorization": "Bearer " + self.tkn})
        uri = self.sw_url + "/workspaces/" + workspace_pk + "/roles/" + role_pk
        try:
            _response = requests.request("PUT", uri, data=role, headers=self.sw_headers, allow_redirects=True)
            try:
                body = json.loads(_response.text)
            except JSONDecodeError as er:
                logger.error(F"{er.__class__.__name__} failed to parse json response: {er}")
                raise er
            logger.info(SVC_RESPONSE.format(body))
            return _response, body
        except Exception as e:
            logger.exception(F"{e.__class__.__name__} update_workspace_role failed with error: {e}")
            raise e
