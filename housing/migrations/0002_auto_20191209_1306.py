# Generated by Django 2.2.7 on 2019-12-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalcategory',
            name='catslug',
            field=models.SlugField(max_length=80, unique=True),
        ),
    ]
