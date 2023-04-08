from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MD1weA10e1zIlWOHi9KcqH9vV1b0DRDkMpyZPm97MmjaTVJ1GCjCJJs5wiNqViVbsEphvXuKzyF4oaZsvNKZq8N00pJQZNuIw',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
