# Generated by Django 4.2.4 on 2023-08-13 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ringtone',
            name='customer',
            field=models.FileField(upload_to='blog'),
        ),
    ]
