# Generated by Django 4.1 on 2022-08-29 23:19

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("categories", "0002_forbiddenword_remove_category_category_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="post_tags",),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=taggit.managers.TaggableManager(
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]