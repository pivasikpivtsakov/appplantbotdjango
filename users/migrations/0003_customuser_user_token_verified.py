# Generated by Django 4.2.5 on 2023-09-29 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_telegram_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_token_verified',
            field=models.BooleanField(default=False),
        ),
    ]
