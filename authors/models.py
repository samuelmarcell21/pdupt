from django.db import models

# Create your models here.

class Authors(models.Model):
    nidn = models.CharField(primary_key=True, max_length=100)
    id_univ = models.CharField(max_length=25)
    name = models.CharField(max_length=255)
    scholar_id = models.CharField(max_length=100, blank=True, null=True)
    sinta_id = models.CharField(max_length=200, blank=True, null=True)
    scopus_id = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=240, blank=True, null=True)
    education = models.CharField(max_length=256, blank=True, null=True)