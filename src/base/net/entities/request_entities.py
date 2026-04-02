from src.base.auto_logger import auto_logger, logger
from src.base.net.entities.base_entity import BaseEntity


class RequestEntity(BaseEntity):
    def __init__(self):
        super(BaseEntity, self).__init__()

    @auto_logger(logger)
    def add_user_to_workspace(self):
        is_folder = bool()
        parent_pk = int()
        role_pks = list()
        username = str()
        self.update({"is_folder": is_folder, "parent_pk": parent_pk, "role_pks": role_pks, "username": username})

        return self

    @auto_logger(logger)
    def create_desktop(self):
        description = str()
        # desktop_state = str()
        is_folder = bool()
        name = str()
        parent_pk = int()
        role_pks = list()
        self.update({"description": description, "is_folder": is_folder, "name": name,
                     "parent_pk": parent_pk, "role_pks": role_pks}) # "desktop_state": desktop_state,

        return self

    @auto_logger(logger)
    def create_device(self):
        business_entity_pk = int()
        description = str()
        device_id = str()
        is_folder = bool()
        model = str()
        name = str()
        parent_pk = int()
        protocol_id = int()
        role_pks = list()
        workspace_pk = int()
        self.update({"business_entity_pk": business_entity_pk, "description": description, "device_id": device_id,
                     "is_folder": is_folder, "model": model, "name": name, "parent_pk": parent_pk,
                     "protocol_id": protocol_id, "role_pks": role_pks, "workspace_pk": workspace_pk})

        return self

    @auto_logger(logger)
    def create_role(self):
        description = str()
        name = str()
        parent_pk = int()
        permissions = list()
        self.update({"description": description, "name": name, "parent_pk": parent_pk, "permissions": permissions})

        return self

    @auto_logger(logger)
    def create_workspace(self):
        description = str()
        is_folder = bool()
        name = str()
        parent_pk = int()
        self.update({"description": description, "is_folder": is_folder, "name": name, "parent_pk": parent_pk})

        return self

    @auto_logger(logger)
    def permissions(self):
        pk = int()
        title = str()
        self.update({"pk": pk, "title": title})

        return self

    @auto_logger(logger)
    def update_desktop(self):
        description = str()
        name = str()
        parent_pk = int()
        role_pks = list()
        self.update({"description": description, "name": name, "parent_pk": parent_pk, "role_pks": role_pks})

        return self

    @auto_logger(logger)
    def update_device(self):
        business_entity_pk = int()
        description = str()
        device_id = str()
        is_folder = bool()
        model = str()
        name = str()
        parent_pk = int()
        protocol_id = int()
        role_pks = list()
        workspace_pk = int()
        self.update({"business_entity_pk": business_entity_pk, "description": description, "device_id": device_id,
                     "is_folder": is_folder, "model": model, "name": name, "parent_pk": parent_pk,
                     "protocol_id": protocol_id, "role_pks": role_pks, "workspace_pk": workspace_pk})

        return self

    @auto_logger(logger)
    def update_role(self):
        description = str()
        name = str()
        parent_pk = int()
        permissions = list()
        self.update({"description": description, "name": name, "parent_pk": parent_pk, "permissions": permissions})

        return self

    @auto_logger(logger)
    def update_user(self):
        fio = str()
        parent_pk = int()
        role_pks = list()
        self.update({"fio": fio, "parent_pk": parent_pk, "role_pks": role_pks})

        return self

    @auto_logger(logger)
    def update_workspace(self):
        description = str()
        name = str()
        parent_pk = int()
        self.update({"description": description, "name": name, "parent_pk": parent_pk})

        return self
