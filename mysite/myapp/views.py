from django.shortcuts import render
from .models import Card, Method, Galki
def index(request):
    card = Card.objects.all()
    method = Method.objects.all()
    galki = Galki.objects.all()
    return render(request, 'myapp/index.html', {'cards': card, 'methods': method, 'galks': galki})

