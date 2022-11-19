from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):


    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))

    if request.GET.get('spec'):
        characters.extend(list('@$*'))

    if request.GET.get('num'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length'))
    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def information(request):
    return render(request, 'generator/info.html')