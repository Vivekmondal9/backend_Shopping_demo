from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import ProductByFilter

urlpatterns=[
    path("products",csrf_exempt(ProductByFilter.as_view()),name="product-by-filter"),
    #  path("productpage",csrf_exempt(ProductPagination.as_view()),name="product-by-filter")
]