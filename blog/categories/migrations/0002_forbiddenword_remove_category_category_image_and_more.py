# Generated by Django 4.1 on 2022-08-29 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ForbiddenWord",
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
                ("forbidden_word", models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(model_name="category", name="category_image",),
        migrations.AlterField(
            model_name="post",
            name="post_category_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="categories.category",
                verbose_name="category",
            ),
        ),
    ]