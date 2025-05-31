from django.db import models

class Employee(models.Model):
    emp_number = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    joining_date = models.DateField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.emp_name
