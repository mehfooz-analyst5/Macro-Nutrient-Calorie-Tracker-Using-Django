from django.shortcuts import render, HttpResponse
from . models import Food



# Create your views here.


def home(request):
    foods = Food.objects.all()

    return render(request, 'app/index.html', {'foods': foods})
