# Generated by Django 2.0.2 on 2019-01-02 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('amount', models.IntegerField()),
                ('summary', models.TextField(blank=True, max_length=600, null=True)),
            ],
            options={
                'permissions': (('view_expense', 'Can view expenses'),),
            },
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_fa', django_jalali.db.models.jDateField(default=django.utils.timezone.now)),
                ('summary', models.TextField(blank=True, max_length=600, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_fund', 'Can view funds'), ('index_fund', 'Can view list of funds')),
            },
        ),
        migrations.AddField(
            model_name='expense',
            name='fund',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fund.Fund'),
        ),
    ]