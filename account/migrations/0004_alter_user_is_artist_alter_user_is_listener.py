# Generated by Django 4.2.4 on 2024-04-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_is_artist_alter_user_is_listener'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_artist',
            field=models.BooleanField(default=False, verbose_name='Is Artist'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_listener',
            field=models.BooleanField(default=False, verbose_name='Is Listener'),
        ),
    ]
