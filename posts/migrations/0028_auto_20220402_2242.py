# Generated by Django 3.2.12 on 2022-04-02 22:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0027_auto_20220402_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 22, 42, 13, 442191)),
        ),
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 22, 42, 13, 441564)),
        ),
    ]
