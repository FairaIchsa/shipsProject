# Generated by Django 4.0.6 on 2022-07-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_remove_node_coord_x_remove_node_coord_y_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searoute',
            name='bandwidth',
        ),
        migrations.RemoveField(
            model_name='searoute',
            name='fullness',
        ),
        migrations.AddField(
            model_name='contractedoffer',
            name='expenses',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
            preserve_default=False,
        ),
    ]