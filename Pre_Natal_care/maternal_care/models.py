from django.db import models

# Create your models here.

class MaternalRecord(models.Model):
    email = models.EmailField(max_length=100)
    month = models.CharField(max_length=50)
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    blood_pressure = models.CharField(max_length=50)
    comment = models.TextField(max_length=100)
    breast_pelvic = models.CharField(max_length=50)
    baby_HeartBeart_rate = models.CharField(max_length=50)
    cervical_exam = models.CharField(max_length=50)
    sti = models.CharField(max_length=50)
    Hiv_result = models.CharField(max_length=50)
    Rh_factor = models.CharField(max_length=50)
    Diabetes = models.CharField(max_length=50)
    Hepatitis_B = models.CharField(max_length=50)
    pregnancy_test = models.CharField(max_length=50)


    def __str__(self):
       return  self.email

    





