import pytest
from tests.factories import PrestashopSynchronizerFactory as PresSyncFactory

pytestmark = pytest.mark.django_db


def test_create_prestashop_synchronizer():
    factory = PresSyncFactory()
    assert factory.entity_id == 1
