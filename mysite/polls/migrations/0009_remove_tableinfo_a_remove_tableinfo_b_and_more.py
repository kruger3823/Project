# Generated by Django 4.1.3 on 2022-12-09 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0008_a_sem_b_sem_c_sem_d_sem_e_sem"),
    ]

    operations = [
        migrations.RemoveField(model_name="tableinfo", name="a",),
        migrations.RemoveField(model_name="tableinfo", name="b",),
        migrations.RemoveField(model_name="tableinfo", name="c",),
        migrations.RemoveField(model_name="tableinfo", name="d",),
        migrations.RemoveField(model_name="tableinfo", name="e",),
    ]
