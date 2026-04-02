import allure
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED
from src.base.net.entities.request_entities import RequestEntity
from src.base.net.entities.response_entities import ResponseEntity

test_case = "[TestWorkspaceEndPoint]"


@allure.feature("REGRESSION")
@allure.story("Workspace End Point should return valid responses.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/swagger_tests/workspace_test.py", test_case)
@allure.description("""
    Regression Tests on Swagger.
    1. Check getWorkspaces 
    2. Check createWorkspace 
    3. Check getWorkspace 
    4. Check updateWorkspace 
    5. Check getWorkspacePermissions 
    6. Check deleteWorkspace 
    """)
@pytest.mark.usefixtures("http_client", "workspace_pk")
@pytest.mark.swagger
@pytest.mark.workspace
@pytest.mark.regression
class TestWorkspaceEndPoint(object):

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaces return valid response.")
    def test_get_workspaces(self, http_client):
        _resp = http_client.get_workspaces()
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        workspace = ResponseEntity().workspace_list()
        assert isinstance(_resp[1]["items"], type(workspace["items"]))
        assert isinstance(_resp[1]["total"], type(workspace["total"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request createWorkspace return valid response.")
    def test_create_workspace(self, http_client):
        description, name = ("Test Description", "Test Name")
        workspace = RequestEntity().create_workspace()
        workspace['description'] = description
        workspace['name'] = name
        workspace['is_folder'] = False
        workspace['parent_pk'] = None
        workspace = workspace.to_json()

        _resp = http_client.post_workspace(workspace)
        assert _resp[0].status_code == 201 or _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        workspace = ResponseEntity().workspace()
        assert isinstance(_resp[1]["description"], type(workspace["description"]))
        assert isinstance(_resp[1]["is_folder"], type(workspace["is_folder"]))
        assert isinstance(_resp[1]["name"], type(workspace["name"]))
        assert isinstance(_resp[1]["owner_pk"], type(workspace["owner_pk"]))
        assert isinstance(_resp[1]["parent_pk"], type(workspace["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(workspace["pk"]))
        assert isinstance(_resp[1]["relative_path"], type(workspace["relative_path"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request getWorkspace return valid response.")
    def test_get_workspace(self, http_client, workspace_pk):
        _resp = http_client.get_workspace(str(workspace_pk))
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        workspace = ResponseEntity().workspace()
        assert isinstance(_resp[1]["description"], type(workspace["description"]))
        assert isinstance(_resp[1]["is_folder"], type(workspace["is_folder"]))
        assert isinstance(_resp[1]["name"], type(workspace["name"]))
        assert isinstance(_resp[1]["owner_pk"], type(workspace["owner_pk"]))
        assert isinstance(_resp[1]["parent_pk"], type(workspace["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(workspace["pk"]))
        assert isinstance(_resp[1]["relative_path"], type(workspace["relative_path"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request updateWorkspace return valid response.")
    def test_update_workspace(self, http_client, workspace_pk):
        description, name = ("Test Description", "Test Name")
        workspace = RequestEntity().update_workspace()
        workspace['description'] = description
        workspace['name'] = name
        workspace['parent_pk'] = None
        workspace = workspace.to_json()
        _resp = http_client.update_workspace(workspace, workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        workspace = ResponseEntity().workspace()
        assert isinstance(_resp[1]["description"], type(workspace["description"]))
        assert isinstance(_resp[1]["is_folder"], type(workspace["is_folder"]))
        assert isinstance(_resp[1]["name"], type(workspace["name"]))
        assert isinstance(_resp[1]["owner_pk"], type(workspace["owner_pk"]))
        assert isinstance(_resp[1]["parent_pk"], type(workspace["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(workspace["pk"]))
        assert isinstance(_resp[1]["relative_path"], type(workspace["relative_path"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request getWorkspacePermissions return valid response.")
    def test_get_workspace_permissions(self, http_client, workspace_pk):
        _resp = http_client.get_workspace_permissions(workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], list)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        permissions = ResponseEntity().permissions()
        if len(_resp[1]) > 0:
            assert isinstance(_resp[1]["description"], type(permissions["description"]))
            assert isinstance(_resp[1]["pk"], type(permissions["pk"]))
            assert isinstance(_resp[1]["title"], type(permissions["title"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request deleteWorkspace return valid response.")
    def test_delete_workspace(self, http_client, workspace_pk):
        _resp = http_client.delete_workspace(workspace_pk)
        assert _resp[0].status_code == 202
        assert _resp[0].ok is True
        assert _resp[1] == "Accepted"
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        logger.info(TEST_CASE_PASSED.format(test_case))
