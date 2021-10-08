from django.db import models

# Create your models here.

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    ninjas = []
    
    def __repr__(self):
        return f"Dojo: {self.name} Ninjas:{self.ninjas}"


class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name='ninjas',on_delete=models.CASCADE)


    def __repr__(self):
        return f"Ninja: {self.first_name} , {self.last_name} , {self.dojo}"