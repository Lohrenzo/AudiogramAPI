# Generated by Django 4.2.4 on 2024-04-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.AddField(
            model_name='user',
            name='is_listener',
            field=models.BooleanField(default=True, verbose_name='Is Listener'),
        ),
    ]
