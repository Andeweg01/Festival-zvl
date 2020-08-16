from django.shortcuts import render, get_object_or_404
from .models import Concert

# Create your views here.

def all_concerts(request):
    """ the view to return concerts.html """

    concerts = Concert.objects.all()

    context = {
        'concerts': concerts,
    }
    
    return render(request, 'concerts/concerts.html', context)


def concert_detail(request, concert_id):
    """ the view to return the detail page concert.html """

    concert = get_object_or_404(Concert, pk=concert_id)

    context = {
        'concert': concert,
    }
    
    return render(request, 'concerts/concert.html', context)
