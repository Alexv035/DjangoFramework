# Generated by Django 4.1.1 on 2022-10-01 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="news",
            old_name="created",
            new_name="create_date",
        ),
    ]
