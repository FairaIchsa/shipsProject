# Generated by Django 4.0.6 on 2022-07-19 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_icebreaker_arrival_icebreaker_departure_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='coord_x',
        ),
        migrations.RemoveField(
            model_name='node',
            name='coord_y',
        ),
        migrations.AddField(
            model_name='node',
            name='coordinates',
            field=models.CharField(default=3, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
