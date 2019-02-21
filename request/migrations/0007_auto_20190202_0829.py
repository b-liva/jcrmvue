# Generated by Django 2.0.2 on 2019-02-02 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0006_requests_parent_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='prefspec',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='reqspec',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='xpref',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='xpref_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.Xpref'),
        ),
        migrations.AlterField(
            model_name='prefspec',
            name='xpref_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.Xpref'),
        ),
        migrations.AlterField(
            model_name='reqspec',
            name='req_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.Requests'),
        ),
        migrations.AlterField(
            model_name='xpref',
            name='req_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.Requests'),
        ),
    ]
