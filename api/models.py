from django.db import models


class Starship(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    starship_class = models.CharField(max_length=255)
    crew_capacity = models.CharField(max_length=255)
    films = models.ManyToManyField('Film', related_name='starships')
    species = models.ManyToManyField('Species', related_name='starships')

    evacuation_capacity = models.PositiveIntegerField()


class Film(models.Model):
    title = models.CharField(max_length=255)
    producer = models.CharField(max_length=255)


class Species(models.Model):
    name = models.CharField(max_length=255)


class Planet(models.Model):
    name = models.CharField(max_length=255)
    population = models.PositiveIntegerField()
