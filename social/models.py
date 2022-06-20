from unicodedata import category
from django.db import models
from django.forms import DateTimeField

# Create your models here

#start photocategories
class Photocategory(models.Model):
    category=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.category
#end photocategories

#this is listhing model
class listhing(models.Model):
          title=models.CharField(max_length=200,null=True)
          discription=models.TextField(null=True)
          image=models.ImageField(upload_to="myimage",null=True)
          created=models.DateTimeField(auto_now_add=True,null=True)
          category=models.ForeignKey(Photocategory,on_delete=models.CASCADE,null=True)
          
          
          def __str__(self):
                    return self.title
#end listhing model 
