from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class problemModel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=356, blank=False)
    difficulty = models.CharField(max_length=16)
    approach = models.TextField()
    language = models.CharField(max_length=10)
    code = models.TextField()
    
    def __str__(self):
        return self.name
    
    