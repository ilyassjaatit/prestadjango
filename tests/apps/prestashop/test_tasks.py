import pytest
from celery.result import EagerResult

from apps.prestashop.tasks import add

pytestmark = pytest.mark.django_db


def test_add(settings):
    settings.CELERY_TASK_ALWAYS_EAGER = True
    task_result = add.delay(4, 4)
    assert isinstance(task_result, EagerResult)
    assert task_result.result == 8
