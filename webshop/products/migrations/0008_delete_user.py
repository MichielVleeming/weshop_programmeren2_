# Generated by Django 2.0.3 on 2018-04-16 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
