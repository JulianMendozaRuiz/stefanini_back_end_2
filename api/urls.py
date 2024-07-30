from django.urls import path
from . import views

urlpatterns = [
    path("product-type/", views.ProductTypeListCreate.as_view(),
         name="productType-view-create"),
    path("product/", views.ProductListCreate.as_view(),
         name="product-view-create"),
]
