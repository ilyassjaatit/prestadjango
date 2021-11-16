import pytest

from apps.prestashop.models import PrestashopConfig
from tests.factories import PrestashopSynchronizerFactory as PresSyncFactory

pytestmark = pytest.mark.django_db
NUM_OF_ITEMS = 10


def test_create_prestashop_synchronizer():
    factory = PresSyncFactory()
    assert factory.entity_id == 1


def test_create_prestashop_config(create_prestashop_config):
    create_prestashop_config
    assert PrestashopConfig.objects.count() == 1
