import allure
import pytest
from config import BaseConfig
from src.base.constants import TEST_CASE_PASSED
from src.base.auto_logger import auto_logger, logger
from src.base.net.entities.request_entities import RequestEntity
from src.base.utils.utils import Utils

test_case = "[TestReceivingEntitiesData]"


@pytest.mark.incremental
@allure.feature("FUNCTIONAL")
@allure.story("User able to ")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/functional_tests/permissions_flow_test.py", test_case)
@allure.description("""
    Functional Test:
    Создание компании -> проверка, что создались у нее роли системные (Админ и Гость) -> 
    создание объекта и рабочего стола -> проверка, что им присвоились системные роли по умолчанию (Админ и Гость) -> 
    Добавление пользователя, с ролью Гость -> проверка, что он может только читать все(например, 
    список объектов, или данные объекта получать) в системе -> Добавить пользователя с ролью Админ и проверить, 
    что под ним можно создавать новые объекты и Рабочие столы.
    """)
@pytest.mark.usefixtures("http_client")
@pytest.mark.functional
class TestPermissions(object):
    workspace_pk = None

    @auto_logger(logger)
    @allure.step("Create workspace and check that by default is has two roles (Admin and Guest).")
    def test_create_company_and_check_roles(self, http_client):
        description, name = ("Test Permission Description", "Test Permissions Name")
        workspace = RequestEntity().create_workspace()
        workspace['description'] = description
        workspace['name'] = name
        workspace['is_folder'] = False
        workspace['parent_pk'] = None
        workspace = workspace.to_json()

        _resp1 = http_client.post_workspace(workspace)
        TestPermissions.workspace_pk = str(_resp1[1]["pk"])

        _resp2 = http_client.get_workspace_roles(TestPermissions.workspace_pk)
        assert len(_resp2[1]["items"]) > 0
        assert _resp2[1]["items"][0]["name"] == "Admin"
        assert _resp2[1]["items"][1]["name"] == "Guest"

    @auto_logger(logger)
    @allure.step("Create desktop and check that by default is has two roles (Admin and Guest).")
    def test_create_desktop_and_check_roles(self, http_client):
        description, name = ("Test Permission Desktop Description", "Test Permission Desktop Name")
        desktop = RequestEntity().create_desktop()
        desktop["description"] = description
        desktop["is_folder"] = False
        desktop["name"] = name
        desktop["parent_pk"] = None
        desktop = desktop.to_json()

        _resp = http_client.post_workspace_desktop(desktop, TestPermissions.workspace_pk)
        assert len(_resp[1]["role_pks"]) == 2

    @auto_logger(logger)
    @allure.step("Create device and check that by default is has two roles (Admin and Guest).")
    def test_create_entity_and_check_roles(self, http_client):
        description, name, model = ("Test Permission Entity Description", "Test Permission Entity Name", "Galileosky")
        device = RequestEntity().create_device()
        device["business_entity_pk"] = Utils.get_random_number()
        device["description"] = description
        device["device_id"] = str(Utils.get_random_number())
        device["is_folder"] = False
        device["model"] = model
        device["name"] = name
        device["parent_pk"] = None
        device["protocol_id"] = 1
        device["workspace_pk"] = int(TestPermissions.workspace_pk)
        device = device.to_json()

        _resp = http_client.post_workspace_entity(device, str(TestPermissions.workspace_pk))
        assert len(_resp[1]["role_pks"]) == 2

    @auto_logger(logger)
    @allure.step("Create user with role Guest and check that it can only view.")
    def test_create_user_guest_and_check_roles(self, http_client):
        workspace_user = RequestEntity().add_user_to_workspace()
        workspace_user['username'] = Utils.random_string_generator()
        workspace_user['is_folder'] = False
        workspace_user['parent_pk'] = None
        workspace_user['role_pks'].insert(0, 19718)
        workspace_user = workspace_user.to_json()

        _resp = http_client.post_workspace_user(workspace_user, str(TestPermissions.workspace_pk))
        assert len(_resp[1]["roles"]) > 0

    @auto_logger(logger)
    @allure.step("Create user with role Admin and check that it can do everything.")
    def test_create_user_admin_and_check_roles(self, http_client):
        workspace_user = RequestEntity().add_user_to_workspace()
        workspace_user['username'] = Utils.random_string_generator()
        workspace_user['is_folder'] = False
        workspace_user['parent_pk'] = None
        workspace_user['role_pks'].insert(0, 19717)
        workspace_user = workspace_user.to_json()

        _resp = http_client.post_workspace_user(workspace_user, str(TestPermissions.workspace_pk))
        assert len(_resp[1]["roles"]) > 0

    logger.info(TEST_CASE_PASSED.format(test_case))
