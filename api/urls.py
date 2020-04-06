from django.urls import path
from api.views import product_list, product_details, category_list, category_details, category_products

urlpatterns = {
    path('products/', product_list),
    path('products/<int:product_id>/', product_details),
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_details),
    path('categories/<int:category_id>/products/', category_products),
}
