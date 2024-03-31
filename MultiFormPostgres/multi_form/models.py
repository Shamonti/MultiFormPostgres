from django.db import models

# Create your models here.
class FormData(models.Model):
  name = models.CharField(max_length = 100, default='')
  phone = models.IntegerField(blank=True, null=True, default=0)
  email = models.CharField(max_length = 100, default='')
  address = models.CharField(max_length=255, default='')  
  class Meta:
        db_table="Persons"