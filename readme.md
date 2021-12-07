# CachedRandomedProducts
App to create random categories, products, randomly change product values and cache page with products.

# How to set up
Install all dependencies
```
pip install -r requirements.txt
```
Set variables in settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DATABASE NAME',
        'USER': 'DATABASE USER NAME',
        'PASSWORD': 'DATABASE USER PASSWORD'
    }
}
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': r'PATH TO CACHE FOLDER',
    }
}
```

# How to use
Command to generate product nomenclature
```
python manage.py create_products <NUMBER_OF_CATEGORIES> <NUMBER_OF_PRODUCTS_IN_EVERY_CATEGORY>
```
Command to update product price, status and remain with new random values
```
python manage.py change_products
```