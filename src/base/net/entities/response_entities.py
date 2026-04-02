from src.base.auto_logger import auto_logger, logger
from src.base.net.entities.base_entity import BaseEntity


class ResponseEntity(BaseEntity):
    def __init__(self):
        super(BaseEntity, self).__init__()

    @auto_logger(logger)
    def desktop(self):
        created_at = str()
        description = str()
        desktop_current_version = int()
        desktop_state = str()
        has_access = bool()
        is_folder = bool()
        name = str()
        owner_id = int()
        parent_pk = int()
        pk = int()
        relative_path = str()
        role_pks = list()
        updated_at = str()
        workspace_id = int()
        self.update({"created_at": created_at, "description": description,
                     "desktop_current_version": desktop_current_version, "desktop_state": desktop_state,
                     "has_access": has_access, "is_folder": is_folder, "name": name, "owner_id": owner_id,
                     "parent_pk": parent_pk, "pk": pk, "relative_path": relative_path, "role_pks": role_pks,
                     "updated_at": updated_at, "workspace_id": workspace_id})

        return self

    @auto_logger(logger)
    def desktop_list(self):
        items = list()
        total = int()
        self.update({"items": items, "total": total})

        return self

    @auto_logger(logger)
    def device(self):
        device_id = str()
        device_pk = int()
        has_access = bool()
        is_folder = bool()
        model = str()
        name = str()
        parent_pk = int()
        pk = int()
        role_pks = list()
        self.update({"device_id": device_id, "device_pk": device_pk, "has_access": has_access, "is_folder": is_folder,
                     "model": model, "name": name, "parent_pk": parent_pk, "pk": pk, "role_pks": role_pks})

        return self

    @auto_logger(logger)
    def device_list(self):
        items = list()
        total = int()
        self.update({"items": items, "total": total})

        return self

    @auto_logger(logger)
    def permissions(self):
        description = str()
        pk = int()
        title = str()
        self.update({"description": description, "pk": pk, "title": title})

        return self

    @auto_logger(logger)
    def role(self):
        description = str()
        is_default = bool()
        is_system = bool()
        name = str()
        parent_pk = int()
        permissions = list()
        pk = int()
        self.update({"description": description, "is_default": is_default, "is_system": is_system, "name": name,
                     "parent_pk": parent_pk, "permissions": permissions, "pk": pk})

        return self

    @auto_logger(logger)
    def role_list(self):
        items = list()
        total = int()
        self.update({"items": items, "total": total})

        return self

    @auto_logger(logger)
    def user(self):
        fio = str()
        is_folder = bool()
        parent_pk = int()
        pk = int()
        roles = list()
        username = str()
        self.update({"fio": fio, "is_folder": is_folder, "parent_pk": parent_pk, "pk": pk, "roles": roles,
                     "username": username})

        return self

    @auto_logger(logger)
    def user_list(self):
        items = list()
        total = int()
        self.update({"items": items, "total": total})

        return self

    @auto_logger(logger)
    def workspace(self):
        description = str()
        is_folder = bool()
        name = str()
        owner_pk = int()
        parent_pk = int()
        pk = int()
        relative_path = str()
        self.update({"description": description, "is_folder": is_folder, "name": name, "owner_pk": owner_pk,
                     "parent_pk": parent_pk, "pk": pk, "relative_path": relative_path})

        return self

    @auto_logger(logger)
    def workspace_list(self):
        items = list()
        total = int()
        self.update({"items": items, "total": total})

        return self
