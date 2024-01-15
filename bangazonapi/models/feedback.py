from enum import Enum
from django.db import models

class Rating(Enum):
    HAPPY = 'happy'
    NEUTRAL = 'neutral'
    SAD = 'sad'

class Feedback(models.Model):
    order_id = models.IntegerField
    review = models.CharField(max_length=255)
    rating = Rating
