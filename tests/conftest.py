import time
import pytest
from src.base.constants import *
from src.base.auto_logger import auto_logger, logger
from src.base.http_cli import HttpClient


@pytest.fixture(scope="class")
@auto_logger(logger)
def r_time_count(request):
    start_time = time.strptime(time.ctime(time.perf_counter()), "%a %b %d %H:%M:%S %Y")
    logger.info(START_TIME.format(start_time.tm_hour, start_time.tm_min, start_time.tm_sec))

    def stop_counter():
        end_time = time.strptime(time.ctime(time.perf_counter()), "%a %b %d %H:%M:%S %Y")
        logger.info(END_TIME.format(end_time.tm_hour, end_time.tm_min, end_time.tm_sec))
        min_ = end_time.tm_min - start_time.tm_min
        sec_ = end_time.tm_sec - start_time.tm_sec
        logger.info(AVERAGE.format(min_, sec_))

    request.addfinalizer(stop_counter)


@pytest.fixture(scope="class")
@auto_logger(logger)
def http_client():
    return HttpClient()


# @pytest.fixture(scope="class")
# @auto_logger(logger)
# def web_driver(request):
#
#     def stop_driver():
#         logger.info("TEST STOP -> Closing browser... {0}".format(driver.name))
#         Browser.close_browser(driver)
#
#     logger.info("Driver is: {0}".format(request.param))
#     driver = WebDriverFactory.get_driver(request.param)
#     request.cls.driver = driver
#     request.addfinalizer(stop_driver)
#     return driver


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" % previousfailed.name)
