from django.db import models

class Product(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=250)
    urlImg = models.TextField('URL_Ссылка')
    price = models.IntegerField('Цена')
    gender = models.CharField('Пол', max_length=50)




    def __str__(self):
        return self.title