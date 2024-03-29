# Generated by Django 5.0.3 on 2024-03-13 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_recipe_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipedata',
            name='recipe_pair',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_data',
        ),
        migrations.RemoveField(
            model_name='recipemedia',
            name='recipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='id',
            field=models.BigAutoField(auto_created=True, default=False, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='RecipeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prep_time', models.TimeField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recipe')),
            ],
        ),
        migrations.DeleteModel(
            name='RecipeDataPair',
        ),
        migrations.DeleteModel(
            name='RecipeData',
        ),
        migrations.DeleteModel(
            name='RecipeMedia',
        ),
    ]
