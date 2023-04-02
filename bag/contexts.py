from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total_cost = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total_cost += quantity * product.price
        product_count += quantity
        bag_items.append(
            {
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            }
        )

    if total_cost > 0:
        total_cost += settings.STANDARD_DELIVERY_CHARGE

    context = {
        'bag_items': bag_items,
        'total_cost': total_cost,
        'product_count': product_count,
    }

    return context
