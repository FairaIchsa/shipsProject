# Generated by Django 4.0.6 on 2022-07-19 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_icebreaker'),
    ]

    operations = [
        migrations.AddField(
            model_name='icebreaker',
            name='arrival',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='icebreaker',
            name='departure',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='icebreaker',
            name='sea_port',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='icebreakers', to='mainapp.node'),
        ),
        migrations.AddField(
            model_name='icebreaker',
            name='sea_route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='icebreakers', to='mainapp.searoute'),
        ),
        migrations.AddField(
            model_name='transportship',
            name='arrival',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='transportship',
            name='departure',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='transportship',
            name='icebreaker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ships', to='mainapp.icebreaker'),
        ),
        migrations.AddField(
            model_name='transportship',
            name='sea_port',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ships', to='mainapp.node'),
        ),
        migrations.AddField(
            model_name='transportship',
            name='sea_route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ships', to='mainapp.searoute'),
        ),
    ]