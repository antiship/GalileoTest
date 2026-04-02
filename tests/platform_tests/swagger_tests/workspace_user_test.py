import allure
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED
from src.base.net.entities.request_entities import RequestEntity
from src.base.net.entities.response_entities import ResponseEntity
from src.base.utils.utils import Utils

test_case = "[TestWorkspaceUserEndPoint]"


@allure.feature("REGRESSION")
@allure.story("WorkspaceUser End Point should return valid responses.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/swagger_tests/workspace_user_test.py", test_case)
@allure.description("""
    Regression Tests on Swagger.
    1. Check getWorkspaceUsers 
    2. Check createWorkspaceUser 
    3. Check deleteWorkspaceUser 
    4. Check getWorkspaceUser 
    5. Check updateWorkspaceUser 
    """)
@pytest.mark.usefixtures("http_client", "workspace_pk")
@pytest.mark.swagger
@pytest.mark.workspace_user
@pytest.mark.regression
class TestWorkspaceUserEndPoint(object):

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaceUsers return valid response.")
    def test_get_workspace_users(self, http_client, workspace_pk):
        _resp = http_client.get_workspace_users(workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        users = ResponseEntity().user_list()
        assert isinstance(_resp[1]["items"], type(users["items"]))
        assert isinstance(_resp[1]["total"], type(users["total"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request createWorkspaceUser return valid response.")
    def test_create_workspace_user(self, http_client, workspace_pk):
        workspace_user = RequestEntity().add_user_to_workspace()
        workspace_user['username'] = Utils.random_string_generator()
        workspace_user['is_folder'] = False
        workspace_user['parent_pk'] = None
        workspace_user['role_pks'].insert(0, 20176)
        workspace_user = workspace_user.to_json()

        _resp = http_client.post_workspace_user(workspace_user, workspace_pk)
        assert _resp[0].status_code == 201 or _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        workspace_user = ResponseEntity().user()
        assert isinstance(_resp[1]["fio"], type(workspace_user["fio"]))
        assert isinstance(_resp[1]["is_folder"], type(workspace_user["is_folder"]))
        assert isinstance(_resp[1]["username"], type(workspace_user["username"]))
        assert isinstance(_resp[1]["parent_pk"], type(workspace_user["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(workspace_user["pk"]))
        assert _resp[1]["roles"], "missed list object roles in json response"
        assert isinstance(_resp[1]["roles"], type(workspace_user["roles"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request deleteWorkspaceUser return valid response.")
    def test_delete_workspace_user(self, http_client, user_pk):
        _resp = http_client.delete_workspace_user(user_pk[1], user_pk[0])
        assert _resp[0].status_code == 202
        assert _resp[0].ok is True
        assert _resp[1] == "Accepted"
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaceUser return valid response.")
    def test_get_workspace_user(self, http_client, user_pk):
        _resp = http_client.get_workspace_user(user_pk[1], user_pk[0])
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        workspace_user = ResponseEntity().user()
        assert isinstance(_resp[1]["fio"], type(workspace_user["fio"]))
        assert isinstance(_resp[1]["is_folder"], type(workspace_user["is_folder"]))
        assert isinstance(_resp[1]["parent_pk"], type(workspace_user["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(workspace_user["pk"]))
        assert isinstance(_resp[1]["username"], type(workspace_user["username"]))
        assert _resp[1]["roles"], "missed list object roles in json response"
        assert isinstance(_resp[1]["roles"], type(workspace_user["roles"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request updateWorkspaceUser return valid response.")
    def test_update_workspace_user(self, http_client, user_pk):
        workspace_user = RequestEntity().update_user()
        workspace_user['fio'] = "Test User"
        workspace_user['parent_pk'] = None
        workspace_user = workspace_user.to_json()

        _resp = http_client.update_workspace_user(workspace_user, user_pk[1], user_pk[0])
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        workspace_user = ResponseEntity().user()
        assert isinstance(_resp[1]["fio"], type(workspace_user["fio"]))
        assert isinstance(_resp[1]["is_folder"], type(workspace_user["is_folder"]))
        assert isinstance(_resp[1]["username"], type(workspace_user["username"]))
        assert isinstance(_resp[1]["parent_pk"], type(workspace_user["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(workspace_user["pk"]))
        assert _resp[1]["roles"], "missed list object roles in json response"
        assert isinstance(_resp[1]["roles"], type(workspace_user["roles"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

