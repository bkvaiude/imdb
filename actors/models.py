from django.utils.translation import ugettext_lazy as _
from django.db import models
from sorl.thumbnail import ImageField
class Actor(models.Model):
    name = models.CharField(_("Actor Name"), max_length=255)
    description = models.TextField(_("Actor Description"))
    file = models.ImageField(_("Actor Banner"), max_length=255)
    career_start_date = models.DateField(_("Actor Career Start Date"))