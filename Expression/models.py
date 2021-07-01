from django.db import models

# Create your models here.
class Expression(models.Model):
    
    title = models.CharField(max_length=255)
    meaning=models.CharField(max_length=255,null=True,blank=True)
    example = models.CharField(max_length=255,null=True,blank=True)
    
    
    
    class Meta:
        verbose_name='expression'
        verbose_name_plural='expressions'
        
    def __str__(self):
        return self.title