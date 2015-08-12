from django.db import models

class Award(models.Model):
    name = models.CharField(_("Award Name"), max_length=255)
    description = models.TextField(_("Award Description"))
    