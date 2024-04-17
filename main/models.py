from django.db import models
from django.contrib.auth.models import AbstractUser

class status(models.Model):
    stat = models.CharField(verbose_name="Статус",max_length=30)
    slug = models.SlugField(verbose_name="URL",max_length=30)

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.stat
    
class clients(models.Model):
    id_score = models.PositiveIntegerField(verbose_name="№ счета")
    first_name = models.CharField(verbose_name="Фамилия", max_length=30)
    middle_name = models.CharField(verbose_name="Имя", max_length=30)
    last_name = models.CharField(verbose_name="Отчество", max_length=30)
    date_birth = models.DateField(verbose_name="День рождения")
    inn = models.PositiveIntegerField(verbose_name="ИНН")
    user = models.CharField(verbose_name="ФИО ответсвенного", max_length=120)
    status = models.ForeignKey(to = status, on_delete=models.CASCADE, verbose_name="Статус")
    slug = models.SlugField(verbose_name="URL",max_length=60)

    class Meta:
        db_table = 'client'
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return f'{self.first_name} {self.middle_name[0]}. {self.last_name[0]}.'
    
class User(AbstractUser):
    full_name = models.CharField(verbose_name="Фамилия Имя Отчество",max_length=150, default="")