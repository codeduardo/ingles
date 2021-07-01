from django.db import models

# Create your models here.
class Verb(models.Model):
    
    word= models.CharField(max_length=200,null=True,blank=True)
    past= models.CharField(max_length=200,null=True,blank=True)
    present= models.CharField(max_length=200,null=True,blank=True)
    future= models.CharField(max_length=200,null=True,blank=True)
    meaning=models.CharField(max_length=200,null=True,blank=True)
    
    class Meta:
        verbose_name='verb'
        verbose_name_plural='verbs'
        
    def __str__(self):
        return self.word
    

