# Generated by Django 4.0.6 on 2022-07-29 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_user_top_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='top_teacher',
        ),
    ]
