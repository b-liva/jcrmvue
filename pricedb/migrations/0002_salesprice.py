# Generated by Django 2.0.2 on 2019-01-27 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pricedb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('price_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricedb.PriceDb')),
            ],
        ),
    ]
