import time
import pytest
import requests
from threading import Thread
from config import BaseConfig
from src.base.utils.http_utils import HttpUtils
from src.base.auto_logger import auto_logger, logger
from src.base.constants import TEST_CASE_PASSED, SVC_RESPONSE


test_case = "[test_load_end_point_multithread]"
num_threads = 10
run_time = time.perf_counter() + 300.0
week = "2023-10-26 10:11:43"
day = "2023-11-01 19:00:00"
month = "2023-10-09 05:48:02"
device_id, fields = (BaseConfig.DEVICE_ID, "DateTime,DeviceID,SignalQuality,DeviceStatus,NumberSatellites,Latitude,"
                                           "Longitude,Speed,GPSTotalMileage")
offset, limit = (0, 1000000)
net_url = "https://" + BaseConfig.BASE_URL + "/workspaces/50/entities/data?"
tkn = HttpUtils.get_authorization_token()
headers = {
    "Authorization": "Bearer " + tkn,
    "Connection": "keep-alive",
    "Host": BaseConfig.BASE_URL,
    "Accept": "*/*",
    "authority": "pm.galileosky.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU, ru; q=0.9, en-US; q=0.8, en; q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.0.0 Safari/537.36"
}
querystring = {
    "DeviceID": device_id,
    "DateTime[gt]": month,
    "fields": fields,
    "sort": "DateTime",
    "offset": offset,
    "limit": limit,
}


@pytest.mark.load
@auto_logger(logger)
def test_load_end_point_multithread():

    while time.perf_counter() < run_time:
        try:
            _response = requests.request("GET", net_url, headers=headers, params=querystring, allow_redirects=True)
            logger.info(SVC_RESPONSE.format(_response.status_code))
            logger.info(SVC_RESPONSE.format(_response.reason))
            logger.info(F"Response time == {_response.elapsed.total_seconds()}")
        except Exception as e:
            logger.error(e)
            pass
    logger.info(TEST_CASE_PASSED.format(test_case))


for i in range(num_threads):
    worker = Thread(target=test_load_end_point_multithread)
    worker.daemon = True
    worker.start()
