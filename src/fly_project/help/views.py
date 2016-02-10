from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from fly_project import settings


@login_required(login_url='/authentication')
def help_page(request):
    return render(request, 'help/view.html',{
        'settings': settings,
    })