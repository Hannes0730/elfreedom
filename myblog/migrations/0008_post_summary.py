# Generated by Django 3.0.7 on 2020-07-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_auto_20200701_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.CharField(default='Input a Short Summary...', max_length=255),
        ),
    ]
