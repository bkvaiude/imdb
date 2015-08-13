from django.db import models
from django.utils.translation import ugettext_lazy as _

class Award(models.Model):
    name = models.CharField(_("Award Name"), max_length=255)
    description = models.TextField(_("Award Description"))
    