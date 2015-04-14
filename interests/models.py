from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=200)


class Country(models.Model):
    name = models.CharField(max_length=200)


class City(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country)


