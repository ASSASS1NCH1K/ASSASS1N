# GGG_PROJECKT/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Главная страница (если нужно)
def home_view(request):
    return render(request, '1.html')

# Страница детальной информации об автомобиле
def car_detail_view(request, car_model):
    car_data_map = {
        'toyota-camry': {
            'title': 'Toyota Camry 2022',
            'brand': 'Toyota',
            'model': 'Camry',
            'year': 2022,
            'color': 'Черный',
            'price': '2 500 000 руб.',
            'image': '1200x900.webp',
            'description': 'Toyota Camry 2022 года - это идеальное сочетание комфорта, надежности и современных технологий. Автомобиль оснащен мощным и экономичным двигателем, просторным салоном с высококачественными материалами отделки и передовыми системами безопасности.',
            'engine': '2.5-литровый 4-цилиндровый, 203 л.с.',
            'transmission': '8-ступенчатая автоматическая',
            'fuel_consumption': '7.8 л/100 км',
            'features': [
                'Кожаный салон',
                'Панорамная крыша',
                'Адаптивный круиз-контроль',
                'Система автоматического торможения',
                'Apple CarPlay/Android Auto',
                'Климат-контроль с двумя зонами',
                'Бесключевой доступ и запуск двигателя',
                'Система контроля слепых зон'
            ],
            'warranty': '3 года или 100 000 км'
        },
        'bmw-x5': {
            'title': 'BMW X5 2021',
            'brand': 'BMW',
            'model': 'X5',
            'year': 2021,
            'color': 'Белый',
            'price': '4 800 000 руб.',
            'image': 'i.webp',
            'description': 'BMW X5 2021 года представляет собой роскошный кроссовер, сочетающий в себе спортивные характеристики, высочайший комфорт и инновационные технологии. Этот автомобиль идеально подходит как для городских поездок, так и для длительных путешествий.',
            'engine': '3.0-литровый 6-цилиндровый турбо, 340 л.с.',
            'transmission': '8-ступенчатая автоматическая Steptronic',
            'fuel_consumption': '9.2 л/100 км',
            'features': [
                'Полный привод xDrive',
                'Пневмоподвеска с адаптивными амортизаторами',
                'Кожаный салон Vernasca',
                'Панорамная стеклянная крыша',
                'Проекционный дисплей',
                'Система Driving Assistant Professional',
                'Система парковки с камерами 360°',
                'Аудиосистема Harman Kardon',
                'Трехзонный климат-контроль',
                'Электропривод крышки багажника'
            ],
            'warranty': '3 года без ограничения пробега'
        },
        'mercedes-e-class': {
            'title': 'Mercedes-Benz E-Class 2023',
            'brand': 'Mercedes-Benz',
            'model': 'E-Class',
            'year': 2023,
            'color': 'Серый',
            'price': '5 200 000 руб.',
            'image': 'gen580_1207605649.jpg',
            'description': 'Mercedes-Benz E-Class 2023 - это эталон роскоши и технологий в бизнес-классе. Автомобиль предлагает непревзойденный комфорт, инновационные системы помощи водителю и элегантный дизайн, который выделяет его на дороге.',
            'engine': '2.0-литровый 4-цилиндровый турбо, 258 л.с.',
            'transmission': '9-ступенчатая автоматическая 9G-TRONIC',
            'fuel_consumption': '7.5 л/100 км',
            'features': [
                'Цифровая приборная панель MBUX',
                'Адаптивная подвеска AIR BODY CONTROL',
                'Кожаный салон ARTICO',
                'Система полуавтономного вождения DRIVE PILOT',
                'Матричные светодиодные фары',
                'Система бесключевого доступа KEYLESS-GO',
                'Аудиосистема Burmester® Surround Sound',
                'Массажные кресла с памятью настроек',
                'Система фильтрации воздуха ENERGIZING AIR CONTROL',
                'Цифровая световая проекция'
            ],
            'warranty': '4 года или 120 000 км'
        }
    }
    
    if car_model in car_data_map:
        car = car_data_map[car_model]
        return render(request, 'car_details.html', {'car': car})
    else:
        return HttpResponse('Автомобиль не найден', status=404)

# Если нужны отдельные функции для каждого автомобиля
def toyota_camry_view(request):
    return car_detail_view(request, 'toyota-camry')

def bmw_x5_view(request):
    return car_detail_view(request, 'bmw-x5')

def mercedes_e_class_view(request):
    return car_detail_view(request, 'mercedes-e-class')