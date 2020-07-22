from django.db import models

# Create your models here.

class Papers(models.Model):
    id_pub = models.CharField(max_length=25, primary_key=True)
    nidn = models.CharField(max_length=25)
    title = models.CharField(max_length=1000)
    cite = models.CharField(max_length=10, blank=True, null=True)
    authors = models.CharField(max_length=2000, null=True)
    keywords = models.CharField(max_length=1000, blank=True, null=True)
    abstract = models.CharField(max_length=10000, blank=True, null=True)
    year = models.CharField(max_length=4, null=True)
    source_title = models.CharField(max_length=1000, blank=True, null=True)
    volume = models.CharField(max_length=100, blank=True, null=True)
    DOI = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=501, blank=True, null=True)

    def __str__(self):
	    return "{}. {}".format(self.id_pub, self.title)

class Topics(models.Model):
    id_publication = models.CharField(max_length=200, primary_key=True)
    id_topic = models.CharField(max_length=10)

    def __str__(self):
	    return "{}. {}".format(self.id_publication, self.id_topic)