import time
import pytest
from config import BaseConfig
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED

test_case = "[test_load_end_point]"
num_threads = 100
run_time = time.perf_counter() + 300.0
timestamp = "2023-10-09 05:48:02"
device_id, time_stamp, fields = (BaseConfig.DEVICE_ID, timestamp, "DateTime,DeviceID,SignalQuality,DeviceStatus,"
                                                                  "NumberSatellites,Latitude,Longitude,Speed,"
                                                                  "GPSTotalMileage")


@pytest.mark.load
@pytest.mark.usefixtures("http_client")
@auto_logger(logger)
def test_load_end_point(http_client):

    while time.perf_counter() < run_time:
        try:
            for x in range(1000000):
                _resp = http_client.get_workspace_entities_data(device_id, time_stamp, fields)
                assert _resp[0].status_code == 200
                assert _resp[0].ok is True
                assert isinstance(_resp[1], dict)
        except Exception as e:
            logger.error(e)
            pass
    logger.info(TEST_CASE_PASSED.format(test_case))
