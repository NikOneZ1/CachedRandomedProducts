from django.urls import path
from django.views.decorators.cache import cache_page
from .views import ProductList

urlpatterns = [
    path('<category>', cache_page(60*5)(ProductList.as_view())),
]
