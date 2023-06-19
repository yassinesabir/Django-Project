from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path('Buyproduct/' , views.Buyproduct),
    path("<int:Product_id>", views.detail, name="Product_detail"),
    path('editProducts/', views.editProducts),
]