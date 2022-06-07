from django.db import models

# Create your models here.

#this is listhing model
class listhing(models.Model):
          title=models.CharField(max_length=200)
          price=models.IntegerField()
          num_bedroom=models.IntegerField()
          num_bathroom=models.IntegerField()
          square_footage=models.IntegerField()
          address=models.CharField(max_length=200)
          #image
          
          
          def __str__(self):
                    return self.title
#end listhing model 
