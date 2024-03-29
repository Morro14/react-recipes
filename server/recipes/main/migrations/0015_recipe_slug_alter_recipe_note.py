# Generated by Django 5.0.3 on 2024-03-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_recipe_cook_time_recipe_prep_time_recipe_servings_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
