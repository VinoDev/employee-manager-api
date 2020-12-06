from django.db import models
import datetime

# Create your models here.

class Employee(models.Model):

    first_name = models.CharField(max_length=80, default="")
    last_name = models.CharField(max_length=80, default="")
    birth_date = models.DateField(default=datetime.date(1900,1,1))
    joined_date = models.DateField(default=datetime.date(1900,1,1))
    salary = models.IntegerField(default=3000)
    occupation = models.CharField(max_length=80, default="")

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def tax(self):
        income_tax = 0.15
        insurance = 0.04
        total_tax = income_tax + insurance
        return self.salary * total_tax
    
    def __str__(self):
        return f"{self.id} - {self.full_name}"

    class Meta():
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'