from django.db import models
from  django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

class Carousel(models.Model):

    img = models.ImageField()
    slider_title = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    aboute = models.TextField(max_length=700)
    price = models.IntegerField(default=1)
    old_price = models.IntegerField(default=2)

    def __str__(self):
        return self.title

class Arrival(models.Model):
    arrivals_img = models.ImageField()
    arrivals_title = models.CharField(max_length=200)
    arrivals_price = models.IntegerField(default=10)
    category = models.ForeignKey("Category",blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.arrivals_title



class Product(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Blog(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    aboute = models.TextField(max_length=700)

    def __str__(self):
        return self.title

class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

 
class Category(models.Model):
    class Meta:
        verbose_name = 'My Category'
        verbose_name_plural = 'My Categorys bob'
        
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name