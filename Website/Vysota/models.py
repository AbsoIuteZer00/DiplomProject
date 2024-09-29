from django.db import models


# Create your models here.


class Company(models.Model):
    """Класс для привязки организации к форме заказа"""
    company = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Заказчики'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.company


class Post(models.Model):
    """Класс для создания публикаций на сайте, через админ панель"""
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
