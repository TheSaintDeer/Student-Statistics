# Generated by Django 5.0.7 on 2024-08-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_student_name_alter_university_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='university',
            options={'ordering': ['name'], 'verbose_name_plural': 'universities'},
        ),
        migrations.AddField(
            model_name='student',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
