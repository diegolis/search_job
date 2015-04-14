from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)


class Job(models.Model):
    date = models.DateTime(auto_now_add=True)
    city = models.ForeignKey(City)
    company = models.ForeignKey(Company)
    subject = models.ForeignKey(Subject)

