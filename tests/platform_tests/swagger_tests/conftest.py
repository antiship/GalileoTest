import pytest
from src.base.auto_logger import auto_logger, logger
from src.base.net.entities.request_entities import RequestEntity
from src.base.utils.utils import Utils


@pytest.fixture(scope="function")
@auto_logger(logger)
def workspace_pk(request, http_client):
    def delete_workspace():
        _r = http_client.delete_workspace(pk)
        assert _r[0].status_code == 202

    description, name = ("Fixture Workspace Description", "Fixture Workspace Name")
    workspace = RequestEntity().create_workspace()
    workspace['description'] = description
    workspace['name'] = name
    workspace['is_folder'] = False
    workspace['parent_pk'] = None
    workspace = workspace.to_json()

    _resp = http_client.post_workspace(workspace)
    assert _resp[0].status_code == 200
    pk = str(_resp[1]["pk"])

    request.addfinalizer(delete_workspace)

    return pk


@pytest.fixture(scope="function")
@auto_logger(logger)
def role_pk(http_client, workspace_pk):
    description, name = ("Fixture Role Description", "Fixture Role Name")
    role = RequestEntity().create_role()
    role["description"] = description
    role["name"] = name
    role["parent_pk"] = None

    permissions = RequestEntity().permissions()
    permissions["pk"] = 1
    permissions["title"] = "View desktop"
    role["permissions"].insert(0, permissions)
    role = role.to_json()

    _resp = http_client.post_workspace_role(role, workspace_pk)
    assert _resp[0].status_code == 200

    return str(_resp[1]["pk"]), workspace_pk


@pytest.fixture(scope="function")
@auto_logger(logger)
def desktop_pk(http_client, workspace_pk):
    description, name = ("Test Desktop Description", "Test Desktop Name")
    desktop = RequestEntity().create_desktop()
    desktop["description"] = description
    desktop["is_folder"] = False
    desktop["name"] = name
    desktop["parent_pk"] = None
    desktop = desktop.to_json()

    _resp = http_client.post_workspace_desktop(desktop, workspace_pk)
    assert _resp[0].status_code == 200

    return str(_resp[1]["pk"])


@pytest.fixture(scope="function")
@auto_logger(logger)
def entity_pk(http_client, workspace_pk):
    description, name, model = ("Test Entity Description", "Test Entity Name", "Galileosky")
    device = RequestEntity().create_device()
    device["business_entity_pk"] = Utils.get_random_number()
    device["description"] = description
    device["device_id"] = str(Utils.get_random_number())
    device["is_folder"] = False
    device["model"] = model
    device["name"] = name
    device["parent_pk"] = None
    device["protocol_id"] = 1
    device["role_pks"].insert(0, 62)
    device["workspace_pk"] = int(workspace_pk)
    device = device.to_json()

    _resp = http_client.post_workspace_entity(device, workspace_pk)
    assert _resp[0].status_code == 200

    return str(_resp[1]["pk"]), str(workspace_pk)


@pytest.fixture(scope="function")
@auto_logger(logger)
def user_pk(http_client, workspace_pk):
    workspace_user = RequestEntity().add_user_to_workspace()
    workspace_user['username'] = Utils.random_string_generator()
    workspace_user['is_folder'] = False
    workspace_user['parent_pk'] = None
    workspace_user = workspace_user.to_json()

    _resp = http_client.post_workspace_user(workspace_user, workspace_pk)
    assert _resp[0].status_code == 200

    return str(_resp[1]["pk"]), str(workspace_pk)
