from django.db import models
from django.db.models import JSONField

# Create your models here.
class Data(models.Model):
	json_data = models.JSONField()