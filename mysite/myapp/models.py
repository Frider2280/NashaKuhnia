from django.db import models

class Card(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'card'

    def __str__(self):
        return self.title

class Method(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'method'

    def __str__(self):
        return self.title

class Galki(models.Model):
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'galki'

    def __str__(self):
        return self.title