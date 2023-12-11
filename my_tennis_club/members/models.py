from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  Age = models.IntegerField(null=True)
  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Court(models.Model):
  courtname = models.CharField(max_length=255)
  kind = models.CharField(max_length=255, null=True)
  location = models.CharField(max_length=255, null=True)
def __str__(self):
  return f"{self.courtname} {self.kind} {self.location}"