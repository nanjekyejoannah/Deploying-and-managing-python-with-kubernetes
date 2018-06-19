from django.db import models
 
class list(models.Model): 
         
    item = models.CharField(max_length=100, unique=True)
    quantity = models.TextField() 
    price = models.TextField()
    created = models.DateTimeField()
 
    def __unicode__(self):
        return self.item