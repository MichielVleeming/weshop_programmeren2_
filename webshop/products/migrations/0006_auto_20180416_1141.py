# Generated by Django 2.0.3 on 2018-04-16 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20180416_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
