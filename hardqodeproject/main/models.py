from django.db import models
from users.models import User, CustomUserManager


class Lesson(models.Model):
    name = models.CharField(max_length=200, default=None, null=True, blank=False)
    link_to_video = models.CharField(max_length=700, default=None, blank=True) #I assumed not all lessons need videos
    view_length_sec = models.IntegerField(default=0, null=True, blank=False)
    viewed = models.ManyToManyField(User, null=True, blank=False, related_name='lessons')
    # product = models.ForeignKey(Product, null=True, blank=False, related_name='lessons', on_delete=models.SET_NULL)
    # todo implement 'is_viewed':bool that is different for each viewer
    # is_viewed = models.ForeignKey(User, null=True, blank=False, related_name='lessson)
    # * i'm not sure how to impletment time of view and other details here


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, default=None, null=True, blank=False) #blank=False means it's required
    owner = models.ForeignKey(User, null=True, blank=False, related_name='products', on_delete=models.SET_NULL)
    lesson = models.ForeignKey(Lesson, null=True, blank=True, related_name='products', on_delete=models.SET_NULL)
    
    #* added `relatd_name` to owner, you can access all user's products by `user.products.all()` without needing a separate object for that.


class Products_Access(models.Model):
    products = models.ManyToManyField(Product, null=True, blank=False, related_name='allowed_products')
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL, related_name='allowed_products')
