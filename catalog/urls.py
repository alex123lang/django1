from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
]
