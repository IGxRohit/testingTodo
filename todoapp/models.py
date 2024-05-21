from django.db import models

# Create your models here.
class table(models.Model):
    title=models.CharField(max_length=200)
    disc=models.TextField()
    date=models.DateField(auto_now_add=True,blank=True)



