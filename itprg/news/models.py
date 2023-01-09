from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField('Title', max_length=150)
    anons = models.CharField('Anons', max_length=250)
    full_tex = models.TextField('Your text')
    date = models.DateField('Date')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

