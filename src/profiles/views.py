from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)


def about(request):
    template = 'about.html'
    context = {}
    return render(request, template, context)


@login_required()
def userProfile(request):
    user = request.user
    template = 'profile.html'
    context = {'user': user}
    return render(request, template, context)
