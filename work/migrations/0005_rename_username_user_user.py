# Generated by Django 4.1.4 on 2022-12-25 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("work", "0004_alter_user_username"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user", old_name="username", new_name="user",
        ),
    ]
