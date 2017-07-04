# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class RegisterForm(models.Model):
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	address=models.TextField()
	image = models.ImageField( upload_to = 'static/img/')
	publish=models.DateTimeField(blank=True)



	def __str__(self):
		return self.first_name

