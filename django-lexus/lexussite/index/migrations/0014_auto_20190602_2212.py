# Generated by Django 2.2 on 2019-06-02 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20190602_2211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'ordering': ('-data', '-status', '-id')},
        ),
    ]