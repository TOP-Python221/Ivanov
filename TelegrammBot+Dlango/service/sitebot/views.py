from django.shortcuts import render
from .models import TgUser

def index(request):
    us = TgUser.objects.all()
    context = {'us' : us}
    return render(request, 'sitebot/index.html', context)
