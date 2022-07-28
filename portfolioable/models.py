from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    notes = models.CharField(max_length=2000)

    def __str__(self):
        return self.name 