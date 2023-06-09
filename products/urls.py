from django.urls import path
from . import views
from .views import AddProductReview

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_review/<int:product_id>/', AddProductReview.as_view(), name='add_review'),
    path('add/', views.add_product, name='add_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
