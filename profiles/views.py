from django.shortcuts import render


def profile(request):
    """ display the user profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
