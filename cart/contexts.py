from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from concerts.models import Concert


def cart_contents(request):

    cart_items = []
    total = 0
    concert_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        concert = get_object_or_404(Concert, pk=item_id)
        total += quantity * concert.concert_price
        concert_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'concert': concert,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'concert_count': concert_count,
        'grand_total': grand_total,
    }

    return context
