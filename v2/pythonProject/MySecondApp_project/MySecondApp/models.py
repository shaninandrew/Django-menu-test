from django.db import models
#  ТУТ МОДЕЛИ ДАННЫХ
## <!-- Шанин Андрей Владимирович  hedgestandart@gmail.com -->

#Класс меню
class CrashMenu (models.Model):
    name = models.CharField( max_length=200 )
    url = models.URLField()
    parent_id = models.IntegerField()

def __str__(self):
    return  ( self.name)

def __dir__():
    pass