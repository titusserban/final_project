# Generated by Django 3.1.6 on 2021-02-20 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='feed',
            new_name='post',
        ),
    ]