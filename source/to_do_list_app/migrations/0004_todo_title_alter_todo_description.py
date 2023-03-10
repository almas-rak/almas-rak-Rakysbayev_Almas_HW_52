# Generated by Django 4.1.5 on 2023-02-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_app', '0003_alter_todo_date_of_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='title',
            field=models.CharField(default='нет заголовка', max_length=200, verbose_name='Заголовок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='Описание'),
        ),
    ]
