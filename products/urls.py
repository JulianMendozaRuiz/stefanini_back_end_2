from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListCreate.as_view(),
         name="product-view-create"),
]
