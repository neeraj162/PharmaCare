# Generated by Django 4.1.4 on 2022-12-25 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("work", "0005_rename_username_user_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=200)),
                ("firstname", models.CharField(max_length=200)),
                ("lastname", models.CharField(max_length=200, null=True)),
                ("password", models.CharField(max_length=200)),
                ("phonecode", models.CharField(max_length=10)),
                ("phNo", models.IntegerField()),
                ("email", models.CharField(max_length=200, unique=True)),
                ("houseNo", models.CharField(max_length=200)),
                ("area", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("pincode", models.IntegerField()),
                ("requirement", models.CharField(max_length=200)),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="User",),
    ]