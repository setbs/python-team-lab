from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):


    context = {
        'title': 'Home - Main',
        'content': "Internet Shop - Home",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - About us',
        'content': "About us",
        'text_on_page': "Text why is this shop so cool and you should use it"
    }

    return render(request, 'main/about.html', context)