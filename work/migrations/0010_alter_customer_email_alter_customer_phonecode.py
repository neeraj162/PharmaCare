# Generated by Django 4.1.4 on 2022-12-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("work", "0009_remove_customer_id_remove_customer_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="customer",
            name="phonecode",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
