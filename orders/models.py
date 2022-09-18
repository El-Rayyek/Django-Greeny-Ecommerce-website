from django.utils import timezone
from django.db import models
from django.utils.translation import gettext as _
from utils.generator import generator
from products.models import Product



# Create your models here.


ORDER_STATUS =(
        ('Recieved','Recieved'),
        ('Processed','Processed'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered')
)


class Order(models.Model):
    code          = models.CharField(_("Order CODE"), max_length=8 ,default=generator)
    order_status  = models.CharField(_("Order Status"), max_length=20,choices=ORDER_STATUS)
    order_time    = models.DateTimeField(_("Order Time"),default=timezone.now)
    delivery_time = models.DateTimeField(_("Delivery Time"),null=True ,blank=True)


class OrderDetail(models.Model):
    order    = models.ForeignKey("Order", verbose_name=_("Order"),related_name='Detail_Order', on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, verbose_name="Product",related_name=_("OrderDetail_product"), on_delete=models.SET_NULL,null=True,blank=True)
    quantity = models.FloatField(_("Quantity"))
    price    = models.FloatField(_("Price"))
    

