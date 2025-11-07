from django.db import models

class Dealership(models.Model):
    name = models.CharField('Имя', max_length=100)
    location = models.CharField('Локация', max_length=100)
    
    def str(self):
        return f"{self.name}"

class Car(models.Model):
    brand = models.CharField('Марка', max_length=100)
    model = models.CharField('Модель', max_length=100)
    year = models.IntegerField('Год')
    color = models.CharField('Цвет', max_length=50)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2) #10 000 000.00
    
    def str(self):
        return f"{self.brand} {self.model}"

class Dealer(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    address = models.CharField('Адрес', max_length=200)
    phone_number = models.CharField('Номер телефона', max_length=20)
    email = models.EmailField('Почта')
    
    def str(self):
        return f"{self.first_name}"

class Client(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, blank=True)
    phone_number = models.CharField('Номер телефона', max_length=20)
    address = models.CharField('Адрес', max_length=200)
    email = models.EmailField('Почта')
    
    def str(self):
        return f"{self.first_name} {self.last_name}"

class Sale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name='Продавец')
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, verbose_name='Дилерский центр')
    sale_amount = models.DecimalField('Цена продажи', max_digits=10, decimal_places=2)
    sale_date = models.DateField('Дата продажи')
    sale_info = models.TextField('Дополнительная информация о продаже', blank=True)
    
    def str(self):
        return f"Продажа {self.car.brand} {self.car.model} клиенту {self.client.first_name} {self.client.last_name}"


# Create your models here.
