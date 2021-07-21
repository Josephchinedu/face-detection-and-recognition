# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Records(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    occupation = models.CharField(max_length=150)
    marital_status = models.CharField(max_length=50)
    national_id = models.FileField(upload_to='images/')

    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name_plural = "Records"
