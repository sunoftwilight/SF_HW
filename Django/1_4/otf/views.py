from django.shortcuts import render
from datetime import datetime

# Create your views here.
def menu(request):
    menus = ['라면', '햄버거', '백반']
    users = []
    today = datetime.today
    context = {
        'menus' : menus,
        'users' : users,
        'today' : today
    }
    return render(request, 'otf/otf.html', context)