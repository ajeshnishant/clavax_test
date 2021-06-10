from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


# Create your models here.
class StudentData(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    studentname = models.CharField(max_length=50)
    fathersname = models.CharField(max_length=50)
    dob = models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.IntegerField()
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    classopted = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(5)])
    marks = models.IntegerField()
    dateenrolled = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.dob.year < 2010:
            raise ValidationError("The date must be above 2010!")
        super(StudentData, self).save(*args, **kwargs)
