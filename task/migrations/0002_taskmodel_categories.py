# Generated by Django 4.2.10 on 2024-03-14 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_categorymodel_tasks'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='categories',
            field=models.ManyToManyField(to='category.categorymodel'),
        ),
    ]
