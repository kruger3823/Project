# Generated by Django 4.1.3 on 2022-12-18 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("polls", "0011_academic_and_proffesional_arabic_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SEM1",
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
                ("sem", models.CharField(max_length=200, null=True)),
                ("m1", models.IntegerField(max_length=20, null=True)),
                ("m2", models.IntegerField(max_length=20, null=True)),
                ("m3", models.IntegerField(max_length=20, null=True)),
                ("m4", models.IntegerField(max_length=20, null=True)),
                ("m5", models.IntegerField(max_length=20, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SEM2",
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
                ("sem", models.CharField(max_length=200, null=True)),
                ("m1", models.IntegerField(max_length=20, null=True)),
                ("m2", models.IntegerField(max_length=20, null=True)),
                ("m3", models.IntegerField(max_length=20, null=True)),
                ("m4", models.IntegerField(max_length=20, null=True)),
                ("m5", models.IntegerField(max_length=20, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SEM3",
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
                ("sem", models.CharField(max_length=200, null=True)),
                ("m1", models.IntegerField(max_length=20, null=True)),
                ("m2", models.IntegerField(max_length=20, null=True)),
                ("m3", models.IntegerField(max_length=20, null=True)),
                ("m4", models.IntegerField(max_length=20, null=True)),
                ("m5", models.IntegerField(max_length=20, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SEM4",
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
                ("sem", models.CharField(max_length=200, null=True)),
                ("m1", models.IntegerField(max_length=20, null=True)),
                ("m2", models.IntegerField(max_length=20, null=True)),
                ("m3", models.IntegerField(max_length=20, null=True)),
                ("m4", models.IntegerField(max_length=20, null=True)),
                ("m5", models.IntegerField(max_length=20, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SEM5",
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
                ("sem", models.CharField(max_length=200, null=True)),
                ("m1", models.IntegerField(max_length=20, null=True)),
                ("m2", models.IntegerField(max_length=20, null=True)),
                ("m3", models.IntegerField(max_length=20, null=True)),
                ("m4", models.IntegerField(max_length=20, null=True)),
                ("m5", models.IntegerField(max_length=20, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SEM6",
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
                ("sem", models.CharField(max_length=200, null=True)),
                ("m1", models.IntegerField(max_length=20, null=True)),
                ("m2", models.IntegerField(max_length=20, null=True)),
                ("m3", models.IntegerField(max_length=20, null=True)),
                ("m4", models.IntegerField(max_length=20, null=True)),
                ("m5", models.IntegerField(max_length=20, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="b", name="user",),
        migrations.RemoveField(model_name="c", name="user",),
        migrations.RemoveField(model_name="d", name="user",),
        migrations.RemoveField(model_name="e", name="user",),
        migrations.DeleteModel(name="A",),
        migrations.DeleteModel(name="B",),
        migrations.DeleteModel(name="C",),
        migrations.DeleteModel(name="D",),
        migrations.DeleteModel(name="E",),
    ]
