import allure
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED

test_case = "[TestVerifyPagination]"
time_stamp = "2023-10-14 06:13:57"
device_id = BaseConfig.DEVICE_ID  # "862631037805040"   # "862631037805040"
device_id, fields = (device_id, "DateTime,DeviceID,Latitude,Longitude,Speed,GPSTotalMileage,SupplyVoltage,"
                                "TerminalTemp,NumberSatellites,SignalQuality,EcoDriveAcceleration")
workspace_id = "50"


@auto_logger(logger)
@allure.step("Make request EntitiesData (from cache) for month period and measure response time in sec.")
def get_data_for_month_from_cache(http_client):
    _resp1 = http_client.get_workspace_entities_data(device_id, time_stamp, fields, workspace_id)
    logger.info(F"Response time {_resp1[0].elapsed.total_seconds()}  with Total {_resp1[1]['Total']}")
    assert _resp1[0].status_code == 200
    _resp2 = http_client.get_workspace_entities_data(device_id, time_stamp, fields, workspace_id)
    logger.info(F"Response time {_resp2[0].elapsed.total_seconds()}  with Total {_resp2[1]['Total']}")
    assert _resp2[0].status_code == 200
    _resp3 = http_client.get_workspace_entities_data(device_id, time_stamp, fields, workspace_id)
    logger.info(F"Response time {_resp3[0].elapsed.total_seconds()}  with Total {_resp3[1]['Total']}")
    assert _resp3[0].status_code == 200
    assert _resp3[0].ok is True
    assert isinstance(_resp3[1], dict)
    TestVerifyPagination.resp_time = _resp3[0].elapsed.total_seconds()


@allure.feature("FUNCTIONAL")
@allure.story("User wants to have ability to get Entities Data by parts using pagination in request.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/functional_tests/verify_pagination_test.py", test_case)
@allure.description("""
    Functional Test:
    - Check that pagination functionality is affected (decreases) on Response Time.
    """)
@pytest.mark.usefixtures("http_client")
@pytest.mark.functional
class TestVerifyPagination(object):

    resp_time = None

    @auto_logger(logger)
    @allure.step("Make request EntitiesData with pagination parameter and measure front of resp_time (cache)")
    def test_get_data_for_month_with_pagination(self, http_client):
        get_data_for_month_from_cache(http_client)
        pagination = (0, 150000)
        _resp = http_client.get_workspace_entities_data(device_id, time_stamp, fields, workspace_id, pagination)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        first_resp_time = _resp[0].elapsed.total_seconds()
        logger.info(F"Response time pagination == {first_resp_time}  with Total {_resp[1]['Total']}")

        assert TestVerifyPagination.resp_time > first_resp_time
        logger.info(F"The response time from cache [{TestVerifyPagination.resp_time}] is grater than response time with"
                    F" pagination [{first_resp_time}]")

        logger.info(TEST_CASE_PASSED.format(test_case))

        # _resp = http_client.get_entities_data(self.device_id, time_stamp, self.fields, pagination)
        # assert _resp[0].status_code == 200
        # assert _resp[0].ok is True
        # assert isinstance(_resp[1], dict)
        # second_resp_time = _resp[0].elapsed.total_seconds()
        # logger.info(F"First response time == {second_resp_time}")

        # _resp = http_client.get_entities_data(self.device_id, time_stamp, self.fields, pagination)
        # assert _resp[0].status_code == 200
        # assert _resp[0].ok is True
        # assert isinstance(_resp[1], dict)
        # third_resp_time = _resp[0].elapsed.total_seconds()
        #
        # _resp = http_client.get_entities_data(self.device_id, time_stamp, self.fields, pagination)
        # assert _resp[0].status_code == 200
        # assert _resp[0].ok is True
        # assert isinstance(_resp[1], dict)
        # four_resp_time = _resp[0].elapsed.total_seconds()

        # assert TestVerifyPagination.resp_time > first_resp_time + second_resp_time + third_resp_time + four_resp_time
        # logger.info(TEST_CASE_PASSED.format(test_case + " /2 step"))
