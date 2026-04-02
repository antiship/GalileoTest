import json
import platform
import random
import string
from src.base.auto_error import AutomationError
from src.base.auto_logger import auto_logger, logger
from src.base.enums import OperationSystem


class Utils:

    @staticmethod
    @auto_logger(logger)
    def detect_os():
        current_platform = platform.system().lower()
        if current_platform == OperationSystem.DARWIN.value:
            return OperationSystem.DARWIN.value
        elif current_platform == OperationSystem.WINDOWS.value:
            return OperationSystem.WINDOWS.value
        elif current_platform == OperationSystem.LINUX.value:
            return OperationSystem.LINUX.value
        else:
            e = AutomationError("The OS is not detected!")
            logger.exception(e)
            raise e

    @staticmethod
    @auto_logger(logger)
    def to_json_dumps(object_, key=None):
        if key:
            return json.dumps(json.loads(json.dumps(object_, default=lambda obj: vars(obj), sort_keys=True, indent=4)
                                         ).pop(key))
        else:
            return json.dumps(object_, default=lambda obj: vars(obj), sort_keys=True, indent=4)

    @staticmethod
    @auto_logger(logger)
    def random_string_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    @auto_logger(logger)
    def get_random_number():
        return random.choice([x for x in range(10000000)])

