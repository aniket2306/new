from django.db import models

class info(models.Model):
    name = models.CharField(max_length = 100)
    member = models.IntegerField(min = 1,max = 20)
    status = models.CharField(default = 'unPaid')
    description = models.CharField(max_length = 500)
    connections = models.ForeignKey(on_delete=models.CASCADE)



    
