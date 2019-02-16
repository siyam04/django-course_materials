from django.shortcuts import render


def home(request):
    """Home Page"""
    template = 'blog/home.html'
    return render(request, template)

