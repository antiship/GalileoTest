from src.base.auto_logger import auto_logger, logger
from src.base.utils.utils import Utils


class BaseEntity(dict):
    def __init__(self):
        super(dict, self).__init__()

    @auto_logger(logger)
    def to_json(self):
        return Utils.to_json_dumps(self)
