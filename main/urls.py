from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('product-detail/<int:id>/', views.product_detail, name='product-detail'),
    path('shoping_cart/', views.shoping_сart, name='shoping_cart'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('delete_product/<int:id>/', views.delete_cart, name='delete_product'),
]