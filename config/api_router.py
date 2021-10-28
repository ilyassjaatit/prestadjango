from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.users.views import UserViewSet
from apps.orders.views import OrderViewSet
from apps.customers.views import CustomerViewSet
from apps.products.views import ProductViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("products", ProductViewSet)
router.register("customers", CustomerViewSet)
router.register("orders", OrderViewSet)

app_name = "api"
urlpatterns = router.urls
