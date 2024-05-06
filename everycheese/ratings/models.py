from django.db import models
from everycheese.cheeses.models import Cheese
from model_utils.models import TimeStampedModel

class Rating(TimeStampedModel):
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()


    def __str__(self):
        return f"Rating for {self.cheese.name}: {self.rating}"
