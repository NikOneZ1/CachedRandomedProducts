from django.views.generic import ListView
from .models import Category, Product


class ProductList(ListView):
    model = Product
    paginate_by = 50

    def get_context_data(self, *args, **kwargs):
        context = super(ProductList, self).get_context_data(*args, **kwargs)
        context['category'] = self.kwargs['category']
        return context

    def get_queryset(self):
        category = Category.objects.get(name=self.kwargs['category'])
        products = Product.objects.filter(category=category)
        return products
