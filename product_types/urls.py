from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductTypeListCreate.as_view(),
         name="productType-view-create"),
]
