# Generated by Django 4.2.1 on 2023-05-13 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("manufactory", "0003_alter_subassembly_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="assembly",
            unique_together={
                ("machine", "subassembly", "process", "start_date", "end_date")
            },
        ),
    ]