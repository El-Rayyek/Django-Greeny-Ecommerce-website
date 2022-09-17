from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class Country(models.Model):
    name = models.CharField(_("Country Name"), max_length=50)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    country = models.ForeignKey("Country", verbose_name=_("Country"),related_name='country_city', on_delete=models.CASCADE)
    name = models.CharField(_("City Name"), max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Cities'