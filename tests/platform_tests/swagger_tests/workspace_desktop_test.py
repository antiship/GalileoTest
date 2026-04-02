import allure
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED
from src.base.net.entities.request_entities import RequestEntity
from src.base.net.entities.response_entities import ResponseEntity

test_case = "[TestWorkspaceDesktopEndPoint]"


@allure.feature("REGRESSION")
@allure.story("WorkspaceDesktop End Point should return valid responses.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/swagger_tests/workspace_desktop_test.py", test_case)
@allure.description("""
    Regression Tests on Swagger.
    1. Check getWorkspaceDesktops 
    2. Check createWorkspaceDesktop 
    3. Check deleteWorkspaceDesktop
    4. Check getWorkspaceDesktop 
    5. Check updateWorkspaceDesktop
    """)
@pytest.mark.usefixtures("http_client", "workspace_pk")
@pytest.mark.swagger
@pytest.mark.desktop
@pytest.mark.regression
class TestWorkspaceDesktopEndPoint(object):

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaceDesktops return valid response.")
    def test_get_workspace_desktops(self, http_client, workspace_pk):
        _resp = http_client.get_workspace_desktops(workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        roles = ResponseEntity().desktop_list()
        assert isinstance(_resp[1]["items"], type(roles["items"]))
        assert isinstance(_resp[1]["total"], type(roles["total"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request createWorkspaceDesktop return valid response.")
    def test_create_workspace_desktop(self, http_client, workspace_pk):
        description, name = ("Test Desktop Description", "Test Desktop Name")
        desktop = RequestEntity().create_desktop()
        desktop["description"] = description
        desktop["is_folder"] = False
        desktop["name"] = name
        desktop["parent_pk"] = None
        desktop = desktop.to_json()

        _resp = http_client.post_workspace_desktop(desktop, workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        desktop = ResponseEntity().desktop()
        assert isinstance(_resp[1]["description"], type(desktop["description"]))
        assert isinstance(_resp[1]["created_at"], type(desktop["created_at"]))
        assert isinstance(_resp[1]["desktop_current_version"], type(desktop["desktop_current_version"]))
        assert isinstance(_resp[1]["desktop_state"], type(desktop["desktop_state"]))
        assert isinstance(_resp[1]["has_access"], type(desktop["has_access"]))
        assert isinstance(_resp[1]["is_folder"], type(desktop["is_folder"]))
        assert isinstance(_resp[1]["name"], type(desktop["name"]))
        assert isinstance(_resp[1]["owner_id"], type(desktop["owner_id"]))
        assert isinstance(_resp[1]["parent_pk"], type(desktop["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(desktop["pk"]))
        assert isinstance(_resp[1]["relative_path"], type(desktop["relative_path"]))
        assert isinstance(_resp[1]["role_pks"], type(desktop["role_pks"]))
        assert isinstance(_resp[1]["updated_at"], type(desktop["updated_at"]))
        assert isinstance(_resp[1]["workspace_id"], type(desktop["workspace_id"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request deleteWorkspaceDesktop return valid response.")
    def test_delete_workspace_desktop(self, http_client, workspace_pk, desktop_pk):
        _resp = http_client.delete_workspace_desktop(workspace_pk, desktop_pk)
        assert _resp[0].status_code == 202
        assert _resp[0].ok is True
        assert _resp[1] == "Accepted"
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaceDesktop return valid response.")
    def test_get_workspace_desktop(self, http_client, workspace_pk, desktop_pk):
        _resp = http_client.get_workspace_desktop(workspace_pk, desktop_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        desktop = ResponseEntity().desktop()
        assert isinstance(_resp[1]["description"], type(desktop["description"]))
        assert isinstance(_resp[1]["created_at"], type(desktop["created_at"]))
        assert isinstance(_resp[1]["desktop_current_version"], type(desktop["desktop_current_version"]))
        assert isinstance(_resp[1]["desktop_state"], type(desktop["desktop_state"]))
        assert isinstance(_resp[1]["has_access"], type(desktop["has_access"]))
        assert isinstance(_resp[1]["is_folder"], type(desktop["is_folder"]))
        assert isinstance(_resp[1]["name"], type(desktop["name"]))
        assert isinstance(_resp[1]["owner_id"], type(desktop["owner_id"]))
        assert isinstance(_resp[1]["parent_pk"], type(desktop["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(desktop["pk"]))
        assert isinstance(_resp[1]["relative_path"], type(desktop["relative_path"]))
        assert isinstance(_resp[1]["role_pks"], type(desktop["role_pks"]))
        assert isinstance(_resp[1]["updated_at"], type(desktop["updated_at"]))
        assert isinstance(_resp[1]["workspace_id"], type(desktop["workspace_id"]))

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request updateWorkspaceDesktop return valid response.")
    def test_update_workspace_desktop(self, http_client, workspace_pk, desktop_pk):
        description, name = ("Test Desktop Description", "Test Desktop Name")
        desktop = RequestEntity().update_desktop()
        desktop['description'] = description
        desktop['name'] = name
        desktop['parent_pk'] = None
        desktop = desktop.to_json()

        _resp = http_client.update_workspace_desktop(desktop, workspace_pk, desktop_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        desktop = ResponseEntity().desktop()
        assert isinstance(_resp[1]["created_at"], type(desktop["created_at"]))
        assert isinstance(_resp[1]["description"], type(desktop["description"]))
        assert isinstance(_resp[1]["desktop_current_version"], type(desktop["desktop_current_version"]))
        assert isinstance(_resp[1]["desktop_state"], type(desktop["desktop_state"]))
        assert isinstance(_resp[1]["has_access"], type(desktop["has_access"]))
        assert isinstance(_resp[1]["is_folder"], type(desktop["is_folder"]))
        assert isinstance(_resp[1]["name"], type(desktop["name"]))
        assert isinstance(_resp[1]["owner_id"], type(desktop["owner_id"]))
        assert isinstance(_resp[1]["parent_pk"], type(desktop["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(desktop["pk"]))
        assert isinstance(_resp[1]["relative_path"], type(desktop["relative_path"]))
        assert isinstance(_resp[1]["role_pks"], type(desktop["role_pks"]))
        assert isinstance(_resp[1]["updated_at"], type(desktop["updated_at"]))
        assert isinstance(_resp[1]["workspace_id"], type(desktop["workspace_id"]))

        logger.info(TEST_CASE_PASSED.format(test_case))
