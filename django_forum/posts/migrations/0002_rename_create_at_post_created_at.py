# Generated by Django 4.1.1 on 2022-09-08 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
