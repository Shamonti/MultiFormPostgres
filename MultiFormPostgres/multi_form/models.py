from django.db import models

# Create your models here.
class FormData(models.Model):
  name = models.CharField(max_length=100),
  phone = models.CharField(max_length = 20),
  email = models.EmailField(),
  address = models.TextField()

class Meta:
  db_table = "Persons"