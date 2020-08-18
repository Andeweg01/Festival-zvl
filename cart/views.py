from django.shortcuts import render

# Create your views here.

def view_cart(request):
    """ the view to return cart.html showing the contents of the chopping cart """
    
    return render(request, 'cart/cart.html')
