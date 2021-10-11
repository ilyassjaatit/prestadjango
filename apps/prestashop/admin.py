from django.contrib import admin
from apps.prestashop.models import PrestashopSynchronizer as PrestaSync

admin.site.register(PrestaSync)
