
customers = Customer.objects.all()


customerByName = Customer.objects.get(name='Erem Karalar')


customerById = Customer.objects.get(id=1)





goals = Goals.objects.first() 
parentName = goals.customer.name



class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(ParentModel)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()

parent.childmodel_set.all()





