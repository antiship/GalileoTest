from src.base.auto_logger import auto_logger, logger
from src.base.net.entities.base_entity import BaseEntity


class DataEntity(BaseEntity):
    def __init__(self):
        super(BaseEntity, self).__init__()

    @auto_logger(logger)
    def device_data(self):
        items = list()
        total = int()
        self.update({"items": items, "total": total})

        return self

    @auto_logger(logger)
    def user_data_field(self):
        name = str()
        type_ = str()
        self.update({"name": name, "type": type_})

        return self
