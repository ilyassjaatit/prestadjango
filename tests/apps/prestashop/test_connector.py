import pytest
from apps.prestashop.connector import PsGetResources

pytestmark = pytest.mark.django_db


def test_ps_get_resources():
    class ResourcesTest(PsGetResources):
        _URL_BASE = "http://localhost.com/"
        RESOURCES_TYPE = "TEST_RESOURCES"
        singular_name = "test_resource"

    resource = ResourcesTest()
    assert resource.url(12) == "http://localhost.com/test_resources/12/"
    assert resource.url() == "http://localhost.com/test_resources/?limit=0,100"
    assert resource.singular_name == "test_resource"
    assert resource.resources_name == resource.RESOURCES_TYPE.lower()
