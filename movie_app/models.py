from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.PositiveIntegerField(null=True)
    budget = models.PositiveIntegerField(default=40_000_000)

    def __str__(self):
        return self.name