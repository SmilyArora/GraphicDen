# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_user_upload_csv_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='file_csv',
            field=models.FileField(default='/no-image.jpg', upload_to='files/'),
        ),
    ]
