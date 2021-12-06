from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(unique=True, max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    status = models.CharField(choices=[('in_stock', 'In stock'), ('out_of_stock', 'Out of stock')], max_length=50)
    remains = models.IntegerField()

    def __str__(self):
        return self.name


# Clear cache, when product object saves
@receiver(post_save, sender=Product)
def clear_cache(**kwargs):
    cache.clear()
