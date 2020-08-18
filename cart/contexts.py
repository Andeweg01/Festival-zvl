from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    total = 0
    concert_count = 0

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'concert_count': concert_count,
        'grand_total': grand_total,
    }

    return context
