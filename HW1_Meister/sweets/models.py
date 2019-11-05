from django.db import models

class SweetManager(models.Manager):
    pass

class Sweet(models.Model):

    name = models.TextField()
    brand = models.TextField()
    expiration_date = models.DateField()
    calories = models.IntegerField()

    objects = SweetManager()

    def __str__(self): return self.name
