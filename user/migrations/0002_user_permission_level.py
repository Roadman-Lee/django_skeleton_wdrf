# Generated by Django 4.0.5 on 2022-06-15 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='permission_level',
            field=models.PositiveIntegerField(default=0, verbose_name='권한'),
        ),
    ]