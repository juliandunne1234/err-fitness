from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView
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


class AddProductReview(CreateView):
    model = Review
    template_name = 'products/add_review.html'
    fields = '__all__'
