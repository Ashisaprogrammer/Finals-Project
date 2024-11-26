from django.db import models
from django.forms import ModelForm,Textarea
class Users_Login(models.Model):
# these are mysq col names
    user_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)

class home_info(models.Model): 
    hid = models.IntegerField()
    cost = models.IntegerField()
    location = models.CharField(max_length=1000) 
    num_rooms = models.IntegerField()
    type_building = models.CharField(max_length=1000) 
    bid = models.CharField(max_length=100)
    num_floors = models.IntegerField() 
    img = models.ImageField(upload_to='static/houses/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.type_building} in {self.location} - ${self.cost}"
    


