import allure
import pytest
from config import BaseConfig
from src.base.constants import TEST_CASE_PASSED
from src.base.auto_logger import auto_logger, logger

test_case = "[TestReceivingEntitiesData]"


@allure.feature("FUNCTIONAL")
@allure.story("User able to get Entities Data for all presented periods of time.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/functional_tests/get_entities_data_test.py", test_case)
@allure.description("""
    Functional Test:
    - Check that request WorkspaceEntitiesData returned data for all possible periods.
    """)
@pytest.mark.usefixtures("http_client")
@pytest.mark.functional
class TestReceivingEntitiesData(object):
    device_id, fields = (BaseConfig.DEVICE_ID, "DateTime,DeviceID,SignalQuality,DeviceStatus,NumberSatellites,Latitude,"
                                               "Longitude,Speed,GPSTotalMileage")

    @auto_logger(logger)
    @allure.step("Verify that entities data for day period is successfully received.")
    def test_get_entity_data_day(self, http_client):
        time_stamp = "2023-11-13 19:00:00"
        _resp = http_client.get_workspace_entities_data(self.device_id, time_stamp, self.fields)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Verify that entities data for 30 minutes period is successfully received.")
    def test_get_entity_data_30_minutes(self, http_client):
        time_stamp = "2023-11-14 05:54:52"
        _resp = http_client.get_workspace_entities_data(self.device_id, time_stamp, self.fields)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)

        logger.info(TEST_CASE_PASSED.format(test_case))

    @auto_logger(logger)
    @allure.step("Verify that entities data for month period is successfully received.")
    def test_get_entity_data_month(self, http_client):
        time_stamp = "2023-10-15 06:13:57"
        _resp = http_client.get_workspace_entities_data(self.device_id, time_stamp, self.fields)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)

        logger.info(TEST_CASE_PASSED.format(test_case))
