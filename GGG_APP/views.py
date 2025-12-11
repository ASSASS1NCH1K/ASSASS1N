from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Car

def home(request):
    """Главная страница со всеми автомобилями и поиском"""
    cars = Car.objects.all().order_by('-year')
    search_query = ''

   
    if request.method == 'GET' and 'q' in request.GET:
        search_query = request.GET.get('q', '').strip()
        if search_query:
           
            cars = Car.objects.filter(
                Q(brand__icontains=search_query) |
                Q(model__icontains=search_query) |
                Q(color__icontains=search_query) |
                Q(description__icontains=search_query)
            ).order_by('-year')

    
    brands = Car.objects.values_list('brand', flat=True).distinct().order_by('brand')

    return render(request, 'index.html', {
        'cars': cars,
        'search_query': search_query,
        'brands': brands,
    }) 


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