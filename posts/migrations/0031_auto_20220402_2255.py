# Generated by Django 3.2.12 on 2022-04-02 22:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0030_auto_20220402_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 22, 55, 39, 86669)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 22, 55, 39, 85999)),
        ),
    ]
