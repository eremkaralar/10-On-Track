from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	
	email = models.CharField(max_length=200, null=True)
	
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name






class Goals(models.Model):
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    goalname=models.CharField(max_length=200,null=False)
    goalstepset=models.IntegerField(null=False)
    complete = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.goalname









