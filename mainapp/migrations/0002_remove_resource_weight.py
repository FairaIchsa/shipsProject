# Generated by Django 4.0.6 on 2022-07-07 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='weight',
        ),
    ]
