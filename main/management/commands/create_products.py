from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django.db import transaction
from ...models import Category, Product
import random


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('categories', type=int, help=u'Quantity of categories')
        parser.add_argument('products', type=int, help=u'Quantity of products in every category')

    def handle(self, *args, **kwargs):
        for i in range(kwargs['categories']):
            with transaction.atomic():
                category = Category.objects.create(name=get_random_string(random.randint(3, 20)))
                for j in range(kwargs['products']):
                    Product.objects.create(name=get_random_string(random.randint(3, 20)),
                                           category=category,
                                           price=random.randrange(1, 10000000)/100,
                                           status=random.choice(['in_stock', 'out_of_stock']),
                                           remains=random.randrange(1, 100000))
