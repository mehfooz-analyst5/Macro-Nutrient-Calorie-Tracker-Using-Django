from django.shortcuts import render, HttpResponse
from . models import Food, Consume



# Create your views here.


def home(request):
    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        food = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=food)
        consume.save()

    return render(request, 'app/index.html', {'foods': foods, 'consumed_food': consumed_food})
