import allure
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED

test_case = "[TestServiceEndPoint]"


@allure.feature("REGRESSION")
@allure.story("Service End Point should return valid responses.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/swagger_tests/service_test.py", test_case)
@allure.description("""
    Regression Tests on Swagger.
    1. Check getHealth 
    2. Check getMetrics 
    """)
@pytest.mark.usefixtures("http_client")
@pytest.mark.swagger
@pytest.mark.service
@pytest.mark.regression
class TestServiceEndPoint(object):

    @auto_logger(logger)
    @allure.step("Check that request getHealth return valid response.")
    def test_get_health(self, http_client):
        _resp = http_client.get_health()
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert _resp[1] == "OK"
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Check that request getMetrics return valid response.")
    def test_get_metrics(self, http_client):
        _resp = http_client.get_metrics()
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], str)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 200

        logger.info(TEST_CASE_PASSED.format(test_case))
