from django.core.management.base import BaseCommand
from django.db import transaction
from ...models import Product
import random


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for obj in products:
            obj.price = random.randrange(1, 10000000)/100
            obj.status = random.choice(['in_stock', 'out_of_stock'])
            obj.remains = random.randrange(1, 100000)
        Product.objects.bulk_update(products, ['price', 'status', 'remains'])
