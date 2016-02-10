from django.shortcuts import render
from django.http import HttpResponse
from fly_project import settings


def land_page(request):
    return render(request, 'landpage/view.html',{
        'settings': settings,
    })