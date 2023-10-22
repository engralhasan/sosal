from django.db import models
from .validators import file_size

# Create your models here.
class videoinput(models.Model):
    caption = models.CharField(max_length=250,null=True,blank=True)
    video= models.FileField(upload_to='video/%y', validators=[file_size])
    
    
    