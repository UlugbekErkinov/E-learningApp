# Generated by Django 4.0.6 on 2022-07-29 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='top_teacher',
            field=models.BooleanField(default=True),
        ),
    ]
