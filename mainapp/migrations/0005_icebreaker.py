# Generated by Django 4.0.6 on 2022-07-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_contractedoffer_landcargo_landroute_offer_shipcargo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icebreaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('speed', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
