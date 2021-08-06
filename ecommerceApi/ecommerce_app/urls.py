from django.urls import path
from .views import ListCategory, DetailCategory, ProductList, DetailProduct

urlpatterns = [ 
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='detailcategory'),
    path('products', ProductList.as_view(), name='productlist'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='detailproduct'),  
]