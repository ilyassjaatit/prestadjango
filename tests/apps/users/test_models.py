from django.contrib.auth import get_user_model

import pytest

from tests.factories import UserFactory

pytestmark = pytest.mark.django_db


def test_create_user():
    user_factory = UserFactory(username="username_test")
    user = get_user_model().objects.get(username=user_factory.username)
    assert user.username == "username_test"