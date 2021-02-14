# Generated by Django 3.1.6 on 2021-02-13 01:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follows', models.ManyToManyField(related_name='followed_by', to='Userprofile.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.fields.CharField, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]