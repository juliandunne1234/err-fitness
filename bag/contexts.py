

def bag_contents(request):

    bag_items = []
    total_cost = 0
    product_count = 0

    if total_cost > 0:
        total_cost += settings.STANDARD_DELIVERY_CHARGE

    context = {
        'bag_items': bag_items,
        'total_cost': total_cost,
        'product_count': product_count,
    }

    return context
