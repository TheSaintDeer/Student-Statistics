# Generated by Django 5.0.7 on 2024-07-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
