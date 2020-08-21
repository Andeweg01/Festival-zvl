from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from concerts.models import Concert


def cart_contents(request):

    cart_items = []
    total = 0
    sub_total = 0
    concert_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        concert = get_object_or_404(Concert, pk=item_id)
        sub_total = quantity * concert.concert_price
        total += quantity * concert.concert_price
        concert_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'concert': concert,
            'sub_total': sub_total,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'sub_total': sub_total,
        'total': total,
        'grand_total': grand_total,
        'concert_count': concert_count,
    }

    return context
