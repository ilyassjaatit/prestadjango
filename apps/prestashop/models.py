from django.db import models
from django.utils.translation import gettext_lazy as _


class PrestashopSynchronizer(models.Model):
    """Synchronize prestashop data with system"""
    PRODUCT = "PRODUCT"
    ENTITY_TYPE_CHOICES = [
        (PRODUCT, _('product'))
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
        help_text=_("Type Entity"),
        choices=ENTITY_TYPE_CHOICES,
    )
    raw_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.entity_type == self.PRODUCT:
            return str(self.entity_type) + " " + self.raw_data['name'][0]['value']
        else:
            self.entity_type

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entity_id', 'prestashop_entity_id', 'entity_type'],
                                    name="prestashop_synchronizer_constraint")
        ]
