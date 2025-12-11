from django.shortcuts import render, get_object_or_404
from .models import Car

def home(request):
    """Главная страница со всеми автомобилями"""
    cars = Car.objects.all().order_by('-year')
    return render(request, 'index.html', {'cars': cars})  

def car_detail(request, car_id):
    """Страница деталей автомобиля"""
    car = get_object_or_404(Car, id=car_id)


    similar_cars = Car.objects.filter(
        brand=car.brand
    ).exclude(id=car.id).order_by('-year')[:3]

    return render(request, 'car_detail.html', {  
        'car': car,
        'similar_cars': similar_cars
    })