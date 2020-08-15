from django.shortcuts import render
from .models import Concert

# Create your views here.

def all_concerts(request):
    """ the view to return concerts.html """

    concerts = Concert.objects.all()

    context = {
        'concerts': concerts,
    }
    
    return render(request, 'concerts/concerts.html', context)
