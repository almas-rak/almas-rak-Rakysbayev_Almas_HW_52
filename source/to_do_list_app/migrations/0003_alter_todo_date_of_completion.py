# Generated by Django 4.1.5 on 2023-02-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_app', '0002_todo_date_of_completion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_of_completion',
            field=models.DateField(blank=True, null=True, verbose_name='Дата завершения'),
        ),
    ]