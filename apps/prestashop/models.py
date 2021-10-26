from django.db import models
from django.utils.translation import gettext_lazy as _


class PrestashopSynchronizer(models.Model):
    """Synchronize prestashop data with system"""
    ENTITY_TYPE_PRODUCT = "PRODUCT"
    ENTITY_TYPE_CHOICES = [
        (ENTITY_TYPE_PRODUCT, _('product'))
    ]
    STATUS_NOT_CREATED = "NOT_CREATED"
    STATUS_CREATED = "CREATED"
    STATUS_CHOICES = [
        (STATUS_NOT_CREATED, _("Not created")),
        (STATUS_CREATED, _("created")),
    ]
    entity_id = models.IntegerField(
        help_text=_("Id entity"),
        editable=False,
        null=True,
        blank=True
    )
    prestashop_entity_id = models.IntegerField(
        help_text=_("Id prestashop_entity_id"),
        editable=False
    )
    entity_type = models.CharField(
        max_length=20,
        editable=False,
        help_text=_("Type Entity"),
        choices=ENTITY_TYPE_CHOICES,
    )
    raw_data = models.JSONField(editable=False)
    status = models.CharField(
        max_length=20,
        help_text=_("Status"),
        editable=False,
        choices=STATUS_CHOICES,
        default=STATUS_NOT_CREATED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.entity_type == self.ENTITY_TYPE_PRODUCT:
            return str(self.entity_type) + " " + self.raw_data['name'][0]['value']
        else:
            self.entity_type

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entity_id', 'prestashop_entity_id', 'entity_type'],
                                    name="prestashop_synchronizer_constraint")
        ]
