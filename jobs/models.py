from django.db import models
from django.contrib import admin
# Create your models here.

class Location(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50)

    def __unicode__(self):
        if self.state:
            return "%s, %s, %s" % (self.city, self.state, self.country)
        else:
            return "%s, %s" % (self.city, self.country)


class Job(models.Model):
    pub_date = models.DateField()
    job_title = models.CharField(max_length=50)
    corp_name = models.CharField(max_length=100)
    job_description = models.TextField()
    location = models.ForeignKey(Location)

    def __unicode__(self):
        return "%s %s (%s) " % (self.job_title, self.corp_name, self.location)


