# Generated by Django 5.0.3 on 2024-03-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_recipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=None, max_length=255, null=True, unique=True),
        ),
    ]
