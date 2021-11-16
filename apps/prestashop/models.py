from django.db import models
from django.utils.translation import gettext_lazy as _

from .config import *

RESOURCES_TYPE_CHOICES = [
    (RESOURCES_TYPE_PRODUCTS, _("Products")),
    (RESOURCES_TYPE_COSTUMERS, _("Costumers")),
    (RESOURCES_TYPE_ORDERS, _("Orders")),
    (RESOURCES_TYPE_ORDER_DETAILS, _("Order Details")),
    (RESOURCES_TYPE_CARTS, _("Carts")),
    (RESOURCES_TYPE_CATEGORIES, _("Categories")),
    (RESOURCES_TYPE_TAGS, _("Tags")),
]

STATUS_CHOICES = [
    (STATUS_NOT_CREATED, _("Not created")),
    (STATUS_CREATED, _("created")),
]


class PrestashopSynchronizer(models.Model):
    """Synchronize prestashop data with system"""

    entity_id = models.IntegerField(help_text=_("Id entity"), editable=False, null=True, blank=True)
    prestashop_entity_id = models.IntegerField(
        help_text=_("Id prestashop_entity_id"), editable=False
    )
    resources_type = models.CharField(
        max_length=20,
        editable=False,
        help_text=_("Type Entity"),
        choices=RESOURCES_TYPE_CHOICES,
    )
    raw_data = models.JSONField(editable=False)
    status = models.CharField(
        max_length=20,
        help_text=_("Status"),
        editable=False,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_CREATED,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.entity_type == RESOURCES_TYPE_PRODUCTS:
            return str(self.entity_type) + " " + self.raw_data["name"][0]["value"]
        elif self.entity_type == RESOURCES_TYPE_COSTUMERS:
            return str(self.entity_type) + " " + self.raw_data["lastname"]
        else:
            return self.entity_type

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["entity_id", "prestashop_entity_id"],
                name="prestashop_synchronizer_constraint",
            )
        ]


class PrestashopConfig(models.Model):
    """
    Configuration of how to map the prestashop resources in the system
    """

    resources_type = models.CharField(
        max_length=20,
        editable=False,
        unique=True,
        help_text=_("Resources Type"),
        choices=RESOURCES_TYPE_CHOICES,
    )
    config = models.JSONField(
        default={
            "data_to_save": [],
        }
    )
    limit_start = models.IntegerField(
        help_text=_("Last limit pagination"), editable=False, default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
