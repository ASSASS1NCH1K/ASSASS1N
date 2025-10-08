from django.db import models


class Dealership(models.Model):
     name = models.CharField('Имя')
     location = models.CharField('Локация')
     def __str__(self):
          return f"{self.name}"
     
class Car(models.Model):
      brand = models.CharField('Марка')
      model = models.CharField('Модель')
      year = models.IntegerField('Год')
      color = models.CharField('Цвет')
      price = models.DecimalField('Цена', max_digits=10, decimal_places=2) #10 000 000.00
      def __str__(self):
          return f"{self.brand}"
      
class Dealer(models.Model):
    first_name = models.CharField('Имя')
    address = models.CharField('Адрес')
    phone_number = models.CharField('Номер телефона')
    email = models.EmailField('Почта')
    def __str__(self):
        return f"{self.first_name}"
    
class Client(models.Model):
    first_name = models.CharField('Имя')
    last_name = models.CharField('Фамилия')
    middle_name = models.CharField('Отчество')
    phone_number = models.CharField('Номер телефона')
    address = models.CharField('Адрес')
    email = models.EmailField('Почта')
    def __str__(self):
        return f"{self.first_name}"

class Sale(models.Model):
     sale_amount = models.DecimalField('Цена продажи', max_digits=10, decimal_places=2) #10 000 000.00
     sale_date   =  models.DateField('Дата продажи')
     def __str__(self):
        return f"{self.first_name}"

       


# Create your models here.
