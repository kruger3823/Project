# Generated by Django 4.1.3 on 2022-12-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0004_tableinfo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="tableinfo", old_name="nameofstudent", new_name="department",
        ),
        migrations.AddField(
            model_name="tableinfo",
            name="semester",
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
