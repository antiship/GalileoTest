import allure
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED
from src.base.net.entities.request_entities import RequestEntity
from src.base.net.entities.response_entities import ResponseEntity
from src.base.utils.utils import Utils

test_case = "[TestWorkspaceEntityEndPoint]"


@allure.feature("REGRESSION")
@allure.story("WorkspaceEntity End Point should return valid responses.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/swagger_tests/workspace_entity_test.py", test_case)
@allure.description("""
    Regression Tests on Swagger.
    1. Check getWorkspaceEntities 
    2. Check createWorkspaceEntity
    3. Check deleteWorkspaceEntity
    4. Check getWorkspaceEntity 
    5. Check updateWorkspaceEntity
    """)
@pytest.mark.usefixtures("http_client", "workspace_pk")
@pytest.mark.swagger
@pytest.mark.entity
@pytest.mark.regression
class TestWorkspaceEntityEndPoint(object):

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaceEntities return valid response.")
    def test_get_workspace_entities(self, http_client, workspace_pk):
        _resp = http_client.get_workspace_entities(workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        devices = ResponseEntity().device_list()
        assert isinstance(_resp[1]["items"], type(devices["items"]))
        assert isinstance(_resp[1]["total"], type(devices["total"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request createWorkspaceEntity return valid response.")
    def test_create_workspace_entity(self, http_client, workspace_pk):
        description, name, model = ("Test Entity Description", "Test Entity Name", "Galileosky")
        device = RequestEntity().create_device()
        device["business_entity_pk"] = Utils.get_random_number()
        device["description"] = description
        device["device_id"] = str(Utils.get_random_number())
        device["is_folder"] = False
        device["model"] = model
        device["name"] = name
        device["parent_pk"] = None
        device["protocol_id"] = 1
        device["role_pks"].insert(0, 62)
        device["workspace_pk"] = int(workspace_pk)
        device = device.to_json()

        _resp = http_client.post_workspace_entity(device, workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        device = ResponseEntity().device()
        assert isinstance(_resp[1]["device_id"], type(device["device_id"]))
        assert isinstance(_resp[1]["device_pk"], type(device["device_pk"]))
        assert isinstance(_resp[1]["has_access"], type(device["has_access"]))
        assert isinstance(_resp[1]["is_folder"], type(device["is_folder"]))
        assert isinstance(_resp[1]["model"], type(device["model"]))
        assert isinstance(_resp[1]["name"], type(device["name"]))
        assert isinstance(_resp[1]["parent_pk"], type(device["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(device["pk"]))
        assert isinstance(_resp[1]["role_pks"], type(device["role_pks"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request deleteWorkspaceEntity return valid response.")
    def test_delete_workspace_entity(self, http_client,  entity_pk):
        _resp = http_client.delete_workspace_entity(entity_pk[1], entity_pk[0])
        assert _resp[0].status_code == 202
        assert _resp[0].ok is True
        assert _resp[1] == "Accepted"
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaceDesktop return valid response.")
    def test_get_workspace_entity(self, http_client, entity_pk):
        _resp = http_client.get_workspace_entity(entity_pk[1], entity_pk[0])
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        device = ResponseEntity().device()
        assert isinstance(_resp[1]["device_id"], type(device["device_id"]))
        assert isinstance(_resp[1]["device_pk"], type(device["device_pk"]))
        assert isinstance(_resp[1]["has_access"], type(device["has_access"]))
        assert isinstance(_resp[1]["is_folder"], type(device["is_folder"]))
        assert isinstance(_resp[1]["model"], type(device["model"]))
        assert isinstance(_resp[1]["name"], type(device["name"]))
        assert isinstance(_resp[1]["parent_pk"], type(device["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(device["pk"]))
        assert isinstance(_resp[1]["role_pks"], type(device["role_pks"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request updateWorkspaceEntity return valid response.")
    def test_update_workspace_entity(self, http_client, entity_pk):
        description, name, model = ("Test Entity Description", "Test Entity Name", "Galileosky")
        device = RequestEntity().update_device()
        device["business_entity_pk"] = Utils.get_random_number()
        device["description"] = description
        device["device_id"] = str(Utils.get_random_number())
        device["is_folder"] = False
        device["model"] = model
        device["name"] = name
        device["parent_pk"] = None
        device["protocol_id"] = 1
        device["role_pks"].insert(0, 62)
        device["workspace_pk"] = int(entity_pk[1])
        device = device.to_json()

        _resp = http_client.update_workspace_entity(device, entity_pk[1], entity_pk[0])
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        device = ResponseEntity().device()
        assert isinstance(_resp[1]["device_id"], type(device["device_id"]))
        assert isinstance(_resp[1]["device_pk"], type(device["device_pk"]))
        assert isinstance(_resp[1]["has_access"], type(device["has_access"]))
        assert isinstance(_resp[1]["is_folder"], type(device["is_folder"]))
        assert isinstance(_resp[1]["model"], type(device["model"]))
        assert isinstance(_resp[1]["name"], type(device["name"]))
        assert isinstance(_resp[1]["parent_pk"], type(device["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(device["pk"]))
        assert isinstance(_resp[1]["role_pks"], type(device["role_pks"]))

        logger.info(TEST_CASE_PASSED.format(test_case))
