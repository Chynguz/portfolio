from django.db import models

# Create your models here.

class Skils(models.Model):
    title = models.CharField(max_length=150)
    
class Messaga(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    text = models.TextField(verbose_name='Сообщение')

class Project(models.Model):
    title = models.CharField(max_length=150)
    discription = models.TextField()
    link = models.TextField()
    image = models.ImageField(upload_to='static')


class About(models.Model):
    name = models.CharField(max_length=100)
    discripshion = models.TextField()
    link = models.TextField()

class About_me(models.Model):
    title = models.CharField('О себе', max_length=100)
    text_about = models.TextField('Текст')
    