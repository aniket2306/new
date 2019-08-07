from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class info(models.Model):
    name = models.CharField(max_length = 100)
    member = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(20)])
    status = models.CharField(max_length = 10,default = 'unPaid')
    description = models.CharField(max_length = 500)
    #connections = models.ForeignKey(on_delete=models.CASCADE)
