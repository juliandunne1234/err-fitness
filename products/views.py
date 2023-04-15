from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .models import Product, Review
from .forms import ReviewForm, ProductForm


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
    form_class = ReviewForm
    template_name = 'products/add_review.html'


@login_required
def add_product(request):
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added a new product.')
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Failed to add product. Confirm the form is valid.')
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only superusers can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Successfully deleted item from ERR Store.')
    return redirect(reverse('products'))
