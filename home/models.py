from django.db import models
# Create your models here.

class Ediprof(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,default='Enter Your Name')
    coverimg =models.ImageField(upload_to='product_picture/', null=True,blank=True,default="cover.png")
    profimg =models.ImageField(upload_to='product_picture/', null=True,blank=True,default="def.png")
    job = models.CharField(max_length=50,null=True,blank=True,default='Enter your job titel')
    scholnam = models.CharField(max_length=50,null=True,blank=True,default='Enter your School name')
    univarName = models.CharField(max_length=50,null=True,blank=True,default='Enter your Collage or univarciti name')
    liveName = models.CharField(max_length=50,null=True,blank=True,default='Enter your Live cuntry')
    fromName = models.CharField(max_length=50,null=True,blank=True,default='Enter your Home Distik')
    
    