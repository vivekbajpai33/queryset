# Generated by Django 4.2.4 on 2023-08-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_ringtone_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='ringtone',
            name='intro',
            field=models.ManyToManyField(to='blog.baseintro'),
        ),
    ]
