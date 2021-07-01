from django.db import models

# Create your models here.
class Word(models.Model):
    
    name= models.CharField(max_length=200)
    meaning=models.CharField(max_length=200,null=True,blank=True)
    
    class Meta:
        verbose_name='word'
        verbose_name_plural='words'
        
    def __str__(self):
        return self.name
    
