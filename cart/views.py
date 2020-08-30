from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from concerts.models import Concert

# Create your views here.


def view_cart(request):
    """ view to return cart showing contents of the shopping cart """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    concert = get_object_or_404(Concert, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'You changed the quantity of tickets \
                         for {concert.friendly_name} to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'You have added \
                         {concert.friendly_name} to the shopping cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product \
        to the specified amount"""

    concert = get_object_or_404(Concert, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'You changed the quantity of tickets \
                         for {concert.friendly_name} to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'You removed \
                         {concert.friendly_name} from your shopping cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """Remove item from the cart"""

    try:
        concert = get_object_or_404(Concert, pk=item_id)
        cart = request.session.get('cart', {})
        redirect_url = request.POST.get('redirect_url')

        cart.pop(item_id)
        messages.success(request, f'You removed {concert.friendly_name} \
                         from your shopping cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing from your shopping cart: {e}')
        return HttpResponse(status=500)
