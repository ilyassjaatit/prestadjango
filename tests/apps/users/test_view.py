import pytest
from apps.users.views import UserViewSet
from tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestUserViewSet:

    def test_me(self, rf):
        view = UserViewSet()
        request = rf.get("/fake-url-user-me/")
        user = UserFactory()
        request.user = user
        view.request = request

        response = view.me(request)

        assert response.data == {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
