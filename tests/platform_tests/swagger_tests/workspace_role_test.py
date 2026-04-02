import allure
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED
from src.base.net.entities.request_entities import RequestEntity
from src.base.net.entities.response_entities import ResponseEntity

test_case = "[TestWorkspaceRoleEndPoint]"


@allure.feature("REGRESSION")
@allure.story("WorkspaceRole End Point should return valid responses.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/swagger_tests/workspace_role_test.py", test_case)
@allure.description("""
    Regression Tests on Swagger.
    1. Check getWorkspaceRoles 
    2. Check createWorkspaceRole 
    3. Check deleteWorkspaceRole
    4. Check getWorkspaceRole 
    5. Check updateWorkspaceRole
    """)
@pytest.mark.usefixtures("http_client", "workspace_pk")
@pytest.mark.swagger
@pytest.mark.role
@pytest.mark.regression
class TestWorkspaceRoleEndPoint(object):

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaceRoles return valid response.")
    def test_get_workspace_roles(self, http_client, workspace_pk):
        _resp = http_client.get_workspace_roles(workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        roles = ResponseEntity().role_list()
        assert isinstance(_resp[1]["items"], type(roles["items"]))
        assert isinstance(_resp[1]["total"], type(roles["total"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request createWorkspaceRole return valid response.")
    def test_create_workspace_role(self, http_client, workspace_pk):
        description, name = ("Test Description", "Test Name")
        role = RequestEntity().create_role()
        role["description"] = description
        role["name"] = name
        role["parent_pk"] = None

        permissions = RequestEntity().permissions()
        permissions["pk"] = 1
        permissions["title"] = "View desktop"
        role["permissions"].insert(0, permissions)
        role = role.to_json()

        _resp = http_client.post_workspace_role(role, workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        role = ResponseEntity().role()
        assert isinstance(_resp[1]["description"], type(role["description"]))
        assert isinstance(_resp[1]["is_default"], type(role["is_default"]))
        assert isinstance(_resp[1]["is_system"], type(role["is_system"]))
        assert isinstance(_resp[1]["name"], type(role["name"]))
        assert isinstance(_resp[1]["parent_pk"], type(role["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["permissions"], type(role["permissions"]))
        assert isinstance(_resp[1]["pk"], type(role["pk"]))

        assert len(_resp[1]["permissions"]) > 0

        permissions = ResponseEntity().permissions()
        assert isinstance(_resp[1]["permissions"][0]["description"], type(permissions["description"]))
        assert isinstance(_resp[1]["permissions"][0]["pk"], type(permissions["pk"]))
        assert isinstance(_resp[1]["permissions"][0]["title"], type(permissions["title"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request deleteWorkspaceRole return valid response.")
    def test_delete_workspace_role(self, http_client, role_pk):
        _resp = http_client.delete_workspace_role(role_pk[1], role_pk[0])
        assert _resp[0].status_code == 202
        assert _resp[0].ok is True
        assert _resp[1] == "Accepted"
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaceRole return valid response.")
    def test_get_workspace_role(self, http_client, role_pk):
        _resp = http_client.get_workspace_role(role_pk[1], role_pk[0])
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        role = ResponseEntity().role()
        assert isinstance(_resp[1]["description"], type(role["description"]))
        assert isinstance(_resp[1]["is_default"], type(role["is_default"]))
        assert isinstance(_resp[1]["is_system"], type(role["is_system"]))
        assert isinstance(_resp[1]["name"], type(role["name"]))
        assert isinstance(_resp[1]["parent_pk"], type(role["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["permissions"], type(role["permissions"]))
        assert isinstance(_resp[1]["pk"], type(role["pk"]))

        assert len(_resp[1]["permissions"]) > 0

        permissions = ResponseEntity().permissions()
        assert isinstance(_resp[1]["permissions"][0]["description"], type(permissions["description"]))
        assert isinstance(_resp[1]["permissions"][0]["pk"], type(permissions["pk"]))
        assert isinstance(_resp[1]["permissions"][0]["title"], type(permissions["title"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request updateWorkspaceRole return valid response.")
    def test_update_workspace_role(self, http_client, role_pk):
        description, name = ("Test Role Description", "Test Role Name")
        role = RequestEntity().update_role()
        role['description'] = description
        role['name'] = name
        role['parent_pk'] = None

        permissions = RequestEntity().permissions()
        permissions["pk"] = 1
        permissions["title"] = "View desktop"
        role["permissions"].insert(0, permissions)
        role = role.to_json()

        _resp = http_client.update_workspace_role(role, role_pk[1], role_pk[0])
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        role = ResponseEntity().role()
        assert isinstance(_resp[1]["description"], type(role["description"]))
        assert isinstance(_resp[1]["is_default"], type(role["is_default"]))
        assert isinstance(_resp[1]["is_system"], type(role["is_system"]))
        assert isinstance(_resp[1]["name"], type(role["name"]))
        assert isinstance(_resp[1]["parent_pk"], type(role["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(role["pk"]))
        assert isinstance(_resp[1]["permissions"], type(role["permissions"]))

        assert len(_resp[1]["permissions"]) > 0

        permissions = ResponseEntity().permissions()
        assert isinstance(_resp[1]["permissions"][0]["description"], type(permissions["description"]))
        assert isinstance(_resp[1]["permissions"][0]["pk"], type(permissions["pk"]))
        assert isinstance(_resp[1]["permissions"][0]["title"], type(permissions["title"]))

        logger.info(TEST_CASE_PASSED.format(test_case))
