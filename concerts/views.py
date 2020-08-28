from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def add_concert(request):
    """ add a concert to the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site manager can add concerts')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES)
        if form.is_valid():
            concert = form.save()
            messages.success(request, 'You added a concert successfully!')
            return redirect(reverse('concert_detail', args=[concert.id]))
        else:
            messages.error(request, 'Failed to add the concert. Please check your form.')
    else:
        form = ConcertForm()

    template = 'concerts/add_concert.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_concert(request, concert_id):
    """ edit a concert in the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site manager can edit concerts')
        return redirect(reverse('home'))

    concert = get_object_or_404(Concert, pk=concert_id)
    if request.method == 'POST':
        form = ConcertForm(request.POST, request.FILES, instance=concert)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated the concert.')
            return redirect(reverse('concert_detail', args=[concert.id]))
        else:
            messages.error(request, 'Failed to update the concert. Please check the form.')
    else:
        form = ConcertForm(instance=concert)
        messages.info(request, f'You are editing {concert.concert_name}')

    template = 'concerts/edit_concert.html'
    context = {
        'form': form,
        'concert': concert,
    }

    return render(request, template, context)


@login_required
def delete_concert(request, concert_id):
    """ delete a concert from the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the site manager can delete concerts')
        return redirect(reverse('home'))

    concert = get_object_or_404(Concert, pk=concert_id)
    concert.delete()
    messages.success(request, 'Concert is deleted!')
    return redirect(reverse('concerts'))
