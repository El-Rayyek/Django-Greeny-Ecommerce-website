from contextlib import nullcontext
from distutils.text_file import TextFile
from django.db import models
from django.utils.translation import gettext as _
from settings.models import Country , City
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

DATA_TYPE = (
    ('Home','Home'),
    ('Office','Office'),
    ('Bussiness','Bussiness'),
    ('Academy','Academy'),
    ('Other','Other'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Profile"),related_name='Profile' ,on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to='profile/',null =True,blank = True)

    def __str__(self) -> str:
        return self.user.username

# create user --------> create profile
@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user = instance)



class UserPhoneNumbers(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user phone"),related_name='user_phone', on_delete=models.CASCADE)
    phone_number = models.CharField(_("Phone Number"), max_length=15)
    type = models.CharField(_("type"), max_length=50 ,choices=DATA_TYPE)

    def __str__(self):
        return f'{self.user.username} - {self.type}'
    
    

class UserAddress(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user address"),related_name='user_address', on_delete=models.CASCADE)
    type = models.CharField(_("type"), max_length=50 ,choices=DATA_TYPE)
    country = models.ForeignKey(Country,related_name='user_country' ,verbose_name=_("Country"), on_delete=models.SET_NULL,null=True)
    city = models.ForeignKey(City, verbose_name=_("City"),related_name='user_city' ,on_delete=models.SET_NULL , null=True)
    state = models.CharField(_("state"), max_length=50)
    region = models.CharField(_("region"), max_length=50)
    street = models.CharField(_("street"), max_length=50)
    note = models.TextField(_("Note") ,max_length=300,null=True , blank=True )


    def __str__(self):
        return f'{self.user.username} - {self.type}'
    