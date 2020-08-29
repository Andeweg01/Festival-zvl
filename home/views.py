from django.shortcuts import render


# Create your views here.
def index(request):
    """ the view to return index.html """

    return render(request, 'home/index.html')
