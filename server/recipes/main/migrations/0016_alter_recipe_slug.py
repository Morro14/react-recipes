# Generated by Django 5.0.3 on 2024-03-16 19:36

from django.db import migrations, models
from main.models import Recipe


def migrate_data_forward(apps, schema_editor):
    for instance in Recipe.objects.all():
        print("Generating slug for %s" % instance)
        instance.save()  # Will trigger slug update


def migrate_data_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0015_recipe_slug_alter_recipe_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="slug",
            field=models.SlugField(auto_created=True, max_length=255),
        ),
        migrations.RunPython(
            migrate_data_forward,
            migrate_data_backward,
        ),
    ]
