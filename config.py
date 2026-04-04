import os
from src import src_dir
from src.base.enums import Environment
from src.base.utils.file_utils import FileUtils


executor = {
    "buildName": "root project- 'galileo_test_framework'",
    "type": "Python 3.12, pytest 7.4.3",
    "IDE": "PyCharm 2023.2.3",
    "builder": "tox 4.11.3",
    "allureReport": "2.24.1"
}

if "ENV" in os.environ.keys():
    env = os.environ.__getitem__("ENV").lower()
else:
    os.environ["ENV"] = Environment.PRODUCTION.value
    env = Environment.PRODUCTION.value


class BaseConfig:
    config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg')
    parser = FileUtils.get_parser(config_file)

    ALLURE_DIR = os.path.join(src_dir, parser.get("PATH", "allure_dir"))
    FileUtils.save_allure_environment(ALLURE_DIR, "env=" + env)
    FileUtils.save_allure_executor(ALLURE_DIR, executor)

    BASE_URL = parser.get("URL's", "base_url")
    SWAGGER_URL = parser.get("URL's", "swagger_url")
    GITLAB_URL = parser.get("URL's", "gitlab_url")
    TOKEN_URL = parser.get("TOKEN", "token_url")

    DEVICE_ID = parser.get("DATA", "device_id")
    USERNAME = parser.get("DATA", "username")
    PASSWORD = parser.get("DATA", "password")
    CLIENT_SECRET = parser.get("DATA", "client_secret")
