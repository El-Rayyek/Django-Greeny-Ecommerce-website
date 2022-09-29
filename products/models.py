from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager



# Create your models here.

FLAG_TYPE = (
    ('New' , 'New'),
    ('Feature' , 'Feature')
)

class Product(models.Model):
    name  = models.CharField(_("Name"), max_length=100)
    SKU   = models.IntegerField(_("SKU"))
    brand = models.ForeignKey("Brand", verbose_name=_("Brand"),related_name='product_brand', on_delete=models.SET_NULL ,null=True ,blank=True)
    price = models.FloatField(_("Price"))
    category = models.ForeignKey("Category", verbose_name=_("Category"),related_name='product_category', on_delete=models.SET_NULL ,null=True ,blank=True)
    desc  = models.TextField(_("Describtion") , max_length=10000)
    tags  = TaggableManager(blank=True)
    flag  = models.CharField(_("Flag"), max_length=10 ,choices=FLAG_TYPE)
    slug = models.SlugField(_("Slug"),null=True,blank=True)

    def save(self):
        self.slug = slugify(self.name)
        return super(Product,self).save()

    def __str__(self) :
        return self.name


class Category(models.Model):
    name  = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to='Category/')

    def __str__(self) :
        return self.name

class Brand(models.Model):
    name  = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to='Brand/',null= True,blank=True)
    slug = models.SlugField(_("slug"),null=True , blank=True )

    def __str__(self) :
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        return super(Brand,self).save()

class Review(models.Model):
    product     = models.ForeignKey("Product", verbose_name=_("Product"),related_name='review_product' ,on_delete=models.SET_NULL ,null =True,blank=True)
    user        = models.ForeignKey(User, verbose_name=_("USER"),related_name='review_author', on_delete=models.SET_NULL,null=True,blank=True)
    rate        = models.IntegerField(_("Review_Rate"),validators=[MaxValueValidator(5),MinValueValidator(0)])
    review      = models.TextField(_("Reveiw_describtion") , max_length=1000)
    create_at = models.DateTimeField(_("Create_at"), default=timezone.now)

    def __str__(self) :
        return f"{self.user.username} - {self.product}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product,verbose_name='Product Image' ,related_name=_("product_image"), on_delete=models.CASCADE)
    image   = models.ImageField(_("Image"), upload_to='product/')

    def __str__(self) :
        return str(self.product)

    
