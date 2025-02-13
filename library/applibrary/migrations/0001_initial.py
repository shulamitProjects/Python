# Generated by Django 4.2.9 on 2024-01-11 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_name", models.CharField(max_length=30)),
                ("age_from", models.IntegerField()),
                ("age_until", models.IntegerField()),
                ("lending_time", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=30)),
                ("birth_date", models.DateField()),
                ("address", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=10)),
                ("password", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("book_name", models.CharField(max_length=30)),
                ("author", models.CharField(max_length=30)),
                ("is_lend", models.BooleanField()),
                ("image", models.CharField(max_length=30)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="applibrary.category",
                    ),
                ),
            ],
        ),
    ]
