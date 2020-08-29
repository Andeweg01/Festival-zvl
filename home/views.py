from django.shortcuts import render


# Create your views here.
def index(request):
    """ the view to return index.html """

    return render(request, 'home/index.html')


def tickets(request):
    """ the view to tickets.html """

    return render(request, 'home/tickets.html')


def sponsoring(request):
    """ the view to sponsoring.html """

    return render(request, 'home/sponsoring.html')


def media(request):
    """ the view to media.html """

    return render(request, 'home/media.html')

