# Generated by Django 5.0.3 on 2024-03-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(auto_created=True, max_length=255),
        ),
    ]