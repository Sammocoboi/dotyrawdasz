from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=100)
    firm = models.ForeignKey(Firm,on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    def __str__(self):
        return self.name
