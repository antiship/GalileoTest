import allure
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED
from src.base.net.entities.data_entities import DataEntity
from src.base.utils.utils import Utils

test_case = "[TestWorkspaceEntityDataEndPoint]"


@allure.feature("REGRESSION")
@allure.story("WorkspaceEntityData End Point should return valid responses.")
@allure.severity(allure.severity_level.BLOCKER)
@allure.testcase(BaseConfig.GITLAB_URL + "platform_tests/swagger_tests/workspace_entity_data_test.py", test_case)
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
@pytest.mark.entity_data
@pytest.mark.regression
class TestWorkspaceEntityDataEndPoint(object):

    @auto_logger(logger)
    @allure.step("Check that request getWorkspaceEntitiesData return valid response.")
    def test_get_workspace_entities_data(self, http_client, workspace_pk):
        time_stamp = "2023-10-30 19:00:00"
        device_id, fields = (str(Utils.get_random_number()), "DateTime,DeviceID,SignalQuality,DeviceStatus,"
                                                             "NumberSatellites,Latitude,Longitude,Speed,GPSTotalMileage")

        _resp = http_client.get_workspace_entities_data(device_id, time_stamp, fields, workspace_pk)
        assert _resp[0].status_code == 200
        assert _resp[0].ok is True
        assert isinstance(_resp[1], dict)
        assert (1000 * _resp[0].elapsed.total_seconds()) <= 1000

        device_data = DataEntity().device_data()
        assert isinstance(_resp[1]["Items"], type(device_data["items"]))
        assert isinstance(_resp[1]["Total"], type(device_data["total"]))

        logger.info(TEST_CASE_PASSED.format(test_case))
