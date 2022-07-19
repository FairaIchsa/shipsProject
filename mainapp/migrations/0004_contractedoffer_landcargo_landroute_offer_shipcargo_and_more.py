# Generated by Django 4.0.6 on 2022-07-19 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_cargo_resource'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractedOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('buy_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('picked', models.BooleanField(default=False)),
                ('departure', models.DateTimeField(null=True)),
                ('arrival', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LandCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.DateTimeField()),
                ('arrival', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LandRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type', models.CharField(choices=[('RW', 'Railway'), ('PL', 'Pipeline')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ShipCargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='supply',
            name='node_0',
        ),
        migrations.RemoveField(
            model_name='supply',
            name='node_1',
        ),
        migrations.RenameField(
            model_name='searoute',
            old_name='node_1',
            new_name='end_node',
        ),
        migrations.RenameField(
            model_name='searoute',
            old_name='node_0',
            new_name='start_node',
        ),
        migrations.AddField(
            model_name='node',
            name='type',
            field=models.CharField(choices=[('SN', 'Sea Node'), ('SP', 'Seaport'), ('LN', 'Land Node'), ('LH', 'Land Hub')], default=4, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transportship',
            name='arc_type',
            field=models.PositiveSmallIntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transportship',
            name='current_load',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transportship',
            name='load_capacity',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transportship',
            name='speed',
            field=models.DecimalField(decimal_places=2, default=15, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Cargo',
        ),
        migrations.DeleteModel(
            name='Supply',
        ),
        migrations.AddField(
            model_name='shipcargo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargos', to='mainapp.transportship'),
        ),
        migrations.AddField(
            model_name='shipcargo',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.resource'),
        ),
        migrations.AddField(
            model_name='offer',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offers', to='mainapp.node'),
        ),
        migrations.AddField(
            model_name='offer',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.resource'),
        ),
        migrations.AddField(
            model_name='landroute',
            name='end_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='land_end_for', to='mainapp.node'),
        ),
        migrations.AddField(
            model_name='landroute',
            name='start_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='land_start_for', to='mainapp.node'),
        ),
        migrations.AddField(
            model_name='landcargo',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargos', to='mainapp.landroute'),
        ),
        migrations.AddField(
            model_name='contractedoffer',
            name='end_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracted_offers_to', to='mainapp.node'),
        ),
        migrations.AddField(
            model_name='contractedoffer',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracted_offers', to='mainapp.transportship'),
        ),
        migrations.AddField(
            model_name='contractedoffer',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.resource'),
        ),
        migrations.AddField(
            model_name='contractedoffer',
            name='start_node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracted_offers_from', to='mainapp.node'),
        ),
    ]