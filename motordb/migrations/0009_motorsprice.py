# Generated by Django 2.0.2 on 2019-01-27 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motordb', '0008_auto_20190127_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotorsPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, unique=True)),
                ('kw', models.DecimalField(decimal_places=1, max_digits=7)),
                ('frame_size', models.CharField(blank=True, max_length=6, null=True)),
                ('speed', models.IntegerField()),
                ('voltage', models.IntegerField(blank=True, null=True)),
                ('ip', models.IntegerField(blank=True, null=True)),
                ('ic', models.IntegerField(blank=True, null=True)),
                ('im', models.CharField(blank=True, max_length=8, null=True)),
                ('yd', models.CharField(blank=True, max_length=10, null=True)),
                ('efficiency', models.FloatField(blank=True, null=True)),
                ('pf', models.FloatField(blank=True, null=True)),
                ('current_ln', models.FloatField(blank=True, null=True)),
                ('current_ls_to_ln', models.FloatField(blank=True, null=True)),
                ('torque_tn', models.FloatField(blank=True, null=True)),
                ('torque_ts_to_tn', models.FloatField(blank=True, null=True)),
                ('torque_tmax_to_tn', models.FloatField(blank=True, null=True)),
                ('torque_rotor_inertia', models.FloatField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('freq', models.FloatField(default=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('summary', models.TextField(blank=True, max_length=700, null=True)),
            ],
        ),
    ]
