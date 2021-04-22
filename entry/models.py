from django.db import models


class Entry(models.Model):
  source=models.CharField(max_length=500, blank=False, default="N/A")
  text=models.CharField(max_length=255, blank=False, default="N/A")
  occupation=models.CharField(max_length=255, blank=False, default="N/A")
  industry=models.CharField(max_length=255, blank=False, default="N/A")
  age=models.IntegerField(blank=False, default=0)
  location=models.CharField(max_length=255, blank=False, default="N/A")
  salary=models.IntegerField(blank=False, default=0)
  paycheck=models.IntegerField(blank=False, default=0)
  debt=models.IntegerField(blank=False, default=0)
  net_worth=models.IntegerField(blank=False, default=0)
  rent=models.IntegerField(blank=False, default=0)
  pronouns=models.CharField(max_length=255, blank=True)
  gender=models.CharField(max_length=255, blank=True)
  other_data=models.JSONField(null=True, blank=True)

  class Meta:
    managed = True
    verbose_name= "Entry"
    verbose_name_plural="Entries"
