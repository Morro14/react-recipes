# Generated by Django 5.0.3 on 2024-03-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_recipeinfo_cook_time_recipeinfo_servings_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeinfo',
            name='cook_time',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='recipeinfo',
            name='prep_time',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='recipeinfo',
            name='total_time',
            field=models.DurationField(null=True),
        ),
    ]
