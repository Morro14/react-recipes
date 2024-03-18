from django.db import models
from datetime import timedelta


# Create your models here.


class Recipe(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, help_text="name")
    slug = models.SlugField(max_length=255, null=True, default=None, unique=True)
    rating = models.FloatField(default=0.0, blank=True)
    description = models.TextField(blank=True)
    ingridients = models.TextField(blank=True)
    directions = models.TextField(blank=True)
    note = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, default=None)

    prep_time = models.DurationField(blank=True, default=timedelta(0))
    cook_time = models.DurationField(blank=True, default=timedelta(0))
    total_time = models.DurationField(blank=True, default=timedelta(0))
    servings = models.IntegerField(blank=True, default=0)

    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Category(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, help_text="name")
    slug = models.SlugField(max_length=255, auto_created=True)
