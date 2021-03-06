# Generated by Django 2.0.2 on 2019-01-06 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_jalali.db.models
import request.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrameSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('amount', models.FloatField()),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_fa', django_jalali.db.models.jDateField(default=django.utils.timezone.now)),
                ('summary', models.TextField(blank=True, max_length=600, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.Customer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('read_payment', 'Can read payment details'), ('index_payment', 'Can see list of payments')),
            },
        ),
        migrations.CreateModel(
            name='PaymentFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to=request.models.upload_location)),
                ('pay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Prefactor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='prefactors')),
                ('summary', models.TextField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrefactorVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='pref_verifications')),
                ('summary', models.TextField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('pref_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Prefactor')),
            ],
        ),
        migrations.CreateModel(
            name='PrefSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('type', models.TextField(default=1)),
                ('price', models.FloatField(blank=True, null=True)),
                ('kw', models.FloatField()),
                ('rpm', models.IntegerField()),
                ('voltage', models.IntegerField(default=380)),
                ('ip', models.IntegerField(blank=True, null=True)),
                ('ic', models.IntegerField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, max_length=500, null=True)),
                ('considerations', models.TextField(blank=True, max_length=500, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to=request.models.upload_location)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('summary', models.TextField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='ReqSpec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('kw', models.FloatField()),
                ('rpm', models.IntegerField()),
                ('voltage', models.IntegerField(default=380)),
                ('ip', models.IntegerField(blank=True, null=True)),
                ('ic', models.IntegerField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, max_length=500, null=True)),
                ('tech', models.BooleanField(default=False)),
                ('price', models.BooleanField(default=False)),
                ('permission', models.BooleanField(default=False)),
                ('sent', models.BooleanField(default=False)),
                ('frame_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='request.FrameSize')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('index_reqspecs', 'can see list of request Specs'), ('read_reqspecs', 'can read request Specs')),
            },
        ),
        migrations.CreateModel(
            name='RequestFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to=request.models.upload_location)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_fa', django_jalali.db.models.jDateField(default=django.utils.timezone.now)),
                ('summary', models.TextField(blank=True, max_length=1000, null=True)),
                ('colleagues', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer.Customer')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='req_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('index_requests', 'can see list of requests'), ('read_requests', 'can read requests'), ('public_requests', 'public in requests'), ('sale_expert', 'can edit own stuff')),
            },
        ),
        migrations.CreateModel(
            name='Xpref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_fa', django_jalali.db.models.jDateField(default=django.utils.timezone.now)),
                ('exp_date_fa', django_jalali.db.models.jDateField(default=django.utils.timezone.now)),
                ('summary', models.TextField(blank=True, max_length=600, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('req_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Requests')),
            ],
            options={
                'permissions': (('index_proforma', 'Can index Proforma'), ('read_proforma', 'Can read Proforma')),
            },
        ),
        migrations.CreateModel(
            name='XprefVerf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='verifications/')),
                ('summary', models.TextField(max_length=1000)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('xpref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Xpref')),
            ],
        ),
        migrations.AddField(
            model_name='requestfiles',
            name='req',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Requests'),
        ),
        migrations.AddField(
            model_name='reqspec',
            name='req_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Requests'),
        ),
        migrations.AddField(
            model_name='reqspec',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='request.ProjectType'),
        ),
        migrations.AddField(
            model_name='proffiles',
            name='prof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Xpref'),
        ),
        migrations.AddField(
            model_name='prefspec',
            name='xpref_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Xpref'),
        ),
        migrations.AddField(
            model_name='prefactor',
            name='request_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Requests'),
        ),
        migrations.AddField(
            model_name='permission',
            name='proforma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Xpref'),
        ),
        migrations.AddField(
            model_name='payment',
            name='xpref_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.Xpref'),
        ),
    ]
