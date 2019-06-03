# Generated by Django 2.2 on 2019-05-11 16:26

from django.db import migrations, models
import django.db.models.deletion
import index.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(help_text='Enter city', max_length=50)),
                ('street', models.CharField(help_text='Enter street', max_length=50)),
                ('house', models.IntegerField(help_text='Enter number of house')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter car name of type', max_length=20)),
                ('coast_per_km', models.IntegerField(help_text='Enter coast per km', validators=[index.validators.validate_more_then_zero])),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(help_text='Enter users login', max_length=20)),
                ('password', models.CharField(help_text='Enter clients password', max_length=20)),
                ('name', models.CharField(help_text='Enter clients name', max_length=20)),
                ('phone_number', models.CharField(help_text='Enter phone number of client', max_length=13)),
                ('roll', models.CharField(choices=[('c', 'Client'), ('a', 'Admin')], default='c', help_text='Enter users site roll', max_length=1)),
            ],
            options={
                'ordering': ['phone_number'],
            },
        ),
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField(help_text='Enter distance in km', validators=[index.validators.validate_more_then_zero])),
                ('from_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from+', to='index.Address')),
                ('to_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to='index.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('a', 'Accepted'), ('r', 'Rejected'), ('u', 'Undefined')], default='u', help_text='Enter request status', max_length=1)),
                ('comment', models.TextField(help_text='Enter comments to request', max_length=256, null=True)),
                ('data', models.DateTimeField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Car')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Client')),
                ('distance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Distance')),
            ],
        ),
    ]