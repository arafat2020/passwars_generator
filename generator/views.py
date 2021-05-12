from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(requist):
    return render(requist,'generator/home.html')

def passwarad(requist):
    chrecter=list('abcdefghijklmnopqrst')
    length= int(requist.GET.get('length'))
    if requist.GET.get('uppercase'):
        chrecter.extend(list('ABCDEFGHIJKLMNOPQEST'))
    if requist.GET.get('Cherecter'):
        chrecter.extend(list('!^@%$#)(*&|":<>?'))
    if requist.GET.get('Number'):
        chrecter.extend(list('1234567890'))
    created_passwrd=" "
    for x in range(length):
        created_passwrd += random.choice(chrecter)

    return render(requist,'generator/passwarad.html',{'passward':created_passwrd})
