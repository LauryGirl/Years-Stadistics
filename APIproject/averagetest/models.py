from django.db import models
from user.models import User

class AverageTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    category = models.CharField(max_length=128)
    
    def __str__(self):
        return f"category: {self.category}, value: {self.value}"

    class Meta:
        verbose_name = "AverageTest"
        verbose_name_plural = 'AverageTests'

class SubjectTest(models.Model):
    name = models.CharField(max_length=128)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    dontcare = models.IntegerField(default=0)
    
    def __str__(self):
        return f"category: {self.name}"

    class Meta:
        verbose_name = "SubjectTest"
        verbose_name_plural = 'SubjectTests'