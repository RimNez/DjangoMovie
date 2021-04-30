from django.db import models


# Create your models here.
class Movie(models.Model):
    # fields for the movie table

    intitulé = models.CharField(max_length=300)
    réalisateur = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    dateRéalisation = models.DateField()
    nombreSorties = models.FloatField()
    image = models.URLField(default=None,null=True)

    def __str__(self):
        return self.intitulé


