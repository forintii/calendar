# В models.py
from django.db import models
from django.contrib.auth.models import User  # Импортируем модель User

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()  # Убедись, что это поле DateField
    color = models.CharField(max_length=7, default='#FFFFFF')  # Цвет заметки (например, для выделения)
    

    def __str__(self):
        return self.title
