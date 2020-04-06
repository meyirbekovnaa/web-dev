from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse,Http404

from api.models import Product, Category


def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_details(request, product_id):
    try:
        products = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return {'error': str(e)}

    return JsonResponse(products.to_json())


def category_list(request):
    categories = Category.objects.all()
    category_json = [category.to_json() for category in categories]
    return JsonResponse(category_json, safe=False)


def category_details(request, category_id):
    try:
        categories = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        raise Http404
    return JsonResponse(categories.to_json())


def category_products(request, category_id):
    products = Product.objects.filter(category=category_id).select_related()
    product_json = [product.to_json() for product in products]
    return JsonResponse(product_json, safe=False)
