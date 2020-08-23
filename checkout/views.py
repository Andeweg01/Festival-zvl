from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in you shopping cart at the moment")
        return redirect(reverse('concerts'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H991lJoES2mMjUQU98Cc2XrFJGZt7aMocRfq15oc4umyDqFdpA7KwULcBKeqy95Eber8gVESl2fcsBDNHtCO35V00VtNWJ4Ur',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
