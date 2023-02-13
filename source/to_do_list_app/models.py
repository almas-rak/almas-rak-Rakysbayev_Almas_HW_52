from django.db import models


# Create your models here.
class Todo(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершено')
    ]

    description = models.CharField(max_length=200, null=False, verbose_name='Описание')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    date_of_completion = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.description} - {self.status}'
