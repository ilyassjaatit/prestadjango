from django.utils.translation import gettext_lazy as _
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
