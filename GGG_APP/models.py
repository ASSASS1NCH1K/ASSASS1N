from django.db import models

class Dealership(models.Model):
    name = models.CharField('Название', max_length=100)
    location = models.CharField('Местоположение', max_length=100)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.CharField(max_length=200, verbose_name="Изображение", blank=True, null=True,
                            help_text="Путь к файлу в папке static/, например: 'images/toyota_camry.jpg'")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class Dealer(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    address = models.CharField('Адрес', max_length=200)
    phone_number = models.CharField('Номер телефона', max_length=20)
    email = models.EmailField('Email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Client(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    last_name = models.CharField('Фамилия', max_length=100)
    middle_name = models.CharField('Отчество', max_length=100, blank=True)
    phone_number = models.CharField('Номер телефона', max_length=20)
    address = models.CharField('Адрес', max_length=200)
    email = models.EmailField('Email')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sale(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Машина")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name="Продавец")
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, verbose_name="Дилерский центр")
    sale_amount = models.DecimalField('Цена продажи', max_digits=10, decimal_places=2)
    sale_date = models.DateField('Дата продажи')
    sale_info = models.TextField('Дополнительная информация о продаже', blank=True)

    def __str__(self):
        return f"Продажа {self.car.brand} {self.car.model} клиенту {self.client.first_name} {self.client.last_name}"