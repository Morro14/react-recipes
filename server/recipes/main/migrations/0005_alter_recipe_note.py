# Generated by Django 5.0.3 on 2024-03-13 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_recipe_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='note',
            field=models.TextField(null=True),
        ),
    ]
