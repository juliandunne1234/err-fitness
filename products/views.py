from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Review
from .forms import ReviewForm


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    product_reviews = Review.objects.filter(product=product)

    context = {
        'product': product,
        'product_reviews': product_reviews,
        'review_form': ReviewForm(),
    }

    return render(request, 'products/product_detail.html', context)
