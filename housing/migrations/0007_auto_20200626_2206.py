# Generated by Django 3.0.7 on 2020-06-27 03:06

from django.db import migrations, models
import housing.models


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0006_auto_20200626_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalproperty',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='rentalproperty',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to=housing.models.get_upload_path),
        ),
    ]
