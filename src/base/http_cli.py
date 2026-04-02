from src.base.net.services.service_svc import ServiceService
from src.base.net.services.user_svc import UserService
from src.base.net.services.workspace_desktop_svc import WorkspaceDesktopService
from src.base.net.services.workspace_entity_data_svc import WorkspaceEntityDataService
from src.base.net.services.workspace_entity_svc import WorkspaceEntityService
from src.base.net.services.workspace_role_svc import WorkspaceRoleService
from src.base.net.services.workspace_svc import WorkspaceService
from src.base.net.services.workspace_user_svc import WorkspaceUserService


class HttpClient(ServiceService, UserService, WorkspaceDesktopService, WorkspaceEntityDataService,
                 WorkspaceEntityService, WorkspaceRoleService, WorkspaceService, WorkspaceUserService):
    def __init__(self):
        super(HttpClient, self).__init__()
        pass
