import allure
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED
from src.base.net.entities.response_entities import ResponseEntity

test_case = "[TestUserEndPoint]"


@allure.feature("REGRESSION")
@allure.story("User End Point should return valid responses.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/swagger_tests/user_test.py", test_case)
@allure.description("""
    Regression Tests on Swagger.
    1. Check getUserProfile 
    """)
@pytest.mark.usefixtures("http_client")
@pytest.mark.swagger
@pytest.mark.user
@pytest.mark.regression
class TestUserEndPoint(object):

    @auto_logger(logger)
    @allure.step("Check that request getUserProfile return valid response.")
    def test_get_user_profile(self, http_client):
        _resp = http_client.get_user_profile()
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        user = ResponseEntity().user()
        assert isinstance(_resp[1]["fio"], type(user["fio"]))
        assert isinstance(_resp[1]["is_folder"], type(user["is_folder"]))
        assert isinstance(_resp[1]["parent_pk"], type(user["parent_pk"])) or _resp[1]["parent_pk"] is None
        assert isinstance(_resp[1]["pk"], type(user["pk"]))
        assert isinstance(_resp[1]["username"], type(user["username"]))
        assert _resp[1]["roles"], "missed list object roles in json response"
        assert isinstance(_resp[1]["roles"], type(user["roles"]))

        logger.info(TEST_CASE_PASSED.format(test_case))
