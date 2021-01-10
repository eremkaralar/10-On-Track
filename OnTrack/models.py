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
    goalcompleteset=models.IntegerField(null=True)
    complete = models.BooleanField(default=False)
    
    def Goals(self, *args, **kwargs):
     qset = super(Goals, self).get_queryset(*args, **kwargs)
     return qset.annotate(division=F('goalcompleteset')/F('goalstepset'))

    
    
    def __str__(self):
        return self.goalname



class Habits(models.Model):
    HABIT_TYPE = (
			('Beneficial','Beneficial'),
			('Detrimental','Detrimental'),
			)

    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    habitname=models.CharField(max_length=200,null=False)
    habittype=models.CharField(max_length=200, null=True, choices=HABIT_TYPE)
    habitcount=models.IntegerField(null=False)
    habitmotivationnote=models.CharField(max_length=500,null=False)

    def __str__(self):
        return self.habitname


    






