# Generated by Django 3.0.7 on 2020-07-08 18:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0012_auto_20200709_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='intro',
        ),
    ]
