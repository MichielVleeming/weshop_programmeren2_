# Generated by Django 2.0.3 on 2018-03-25 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
