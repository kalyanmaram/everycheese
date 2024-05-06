from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField
from django.urls import reverse
from django.db.models import Avg

class Cheese(TimeStampedModel):
    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)
    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)
    country_of_origin = CountryField("Country of Origin", blank=True)

    def get_absolute_url(self):
        return reverse('cheeses:detail', kwargs={"slug": self.slug})

    def calculate_average_rating(self):
        average_rating = Rating.objects.filter(cheese_id=self.id).aggregate(average_rating=Avg('rating'))['average_rating']
        if average_rating is not None:
            return int(average_rating)
        else:
            return 0

   
    def __str__(self):
        return self.name

class Rating(models.Model):
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    rating = models.IntegerField("Rating", default=0)
