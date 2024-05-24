from django.urls import path
from .views import CategoryListCreate, CategoryDetailUpdateDelete, ProductListCreate, ProductDetailUpdateDelete, ReviewListCreate, ReviewDetailUpdateDelete, ProductReviews

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:id>/', CategoryDetailUpdateDelete.as_view(), name='category-detail-update-delete'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:id>/', ProductDetailUpdateDelete.as_view(), name='product-detail-update-delete'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:id>/', ReviewDetailUpdateDelete.as_view(), name='review-detail-update-delete'),
    path('products/reviews/', ProductReviews.as_view(), name='product-reviews'),
]
