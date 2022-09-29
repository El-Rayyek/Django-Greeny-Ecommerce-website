from unittest.util import _MAX_LENGTH
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

class Company(models.Model):
    name = models.CharField(_("Name Company"), max_length=50)
    logo = models.ImageField(_("Logo"), upload_to='company')
    about = models.TextField(_("about"), null=True,blank=True , max_length = 300)
    fb_link = models.URLField(_("Face Book"), null=True,blank=True , max_length=200)
    tw_link = models.URLField(_("Twitter"), null=True,blank=True , max_length=200)
    ins_link = models.URLField(_("Instegram"), null=True,blank=True , max_length=200)
    email = models.EmailField(_("Email"), null=True,blank=True , max_length=200)
    phone = models.CharField(_("Phone"), max_length=50)
    address = models.CharField(_("Address"), max_length=50)

    def __str__(self) -> str:
        return self.name