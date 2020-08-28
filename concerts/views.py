from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Concert, Edition, Location

from .forms import ConcertForm


def all_concerts(request):
    """ the view to return concerts.html """

    concerts = Concert.objects.all()
    edition = None
    location = None

    if request.GET:
        if 'edition' in request.GET:
            editions = request.GET['edition'].split(',')
            concerts = concerts.filter(edition__name__in=editions)
            editions = Edition.objects.filter(name__in=editions)

    if request.GET:
        if 'location' in request.GET:
            locations = request.GET['location'].split(',')
            concerts = concerts.filter(location__loc_name__in=locations)
            locations = Location.objects.filter(loc_name__in=locations)

    context = {
        'concerts': concerts,
    }

    return render(request, 'concerts/concerts.html', context)


def concert_detail(request, concert_id):
    """ the view to return the detail page concert_detail.html """

    concert = get_object_or_404(Concert, pk=concert_id)

    context = {
        'concert': concert,
    }

    return render(request, 'concerts/concert_detail.html', context)


def add_concert(request):
    """ add a concert to the database """
    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You added a concert successfully!')
            return redirect(reverse('add_concert'))
        else:
            messages.error(request, 'Failed to add the concert. Please check your form.')
    else:
        form = ConcertForm()

    template = 'concerts/add_concert.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
