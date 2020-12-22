from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

# Create your views here.

from .models import *
from .forms import *





def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='login')
def get_full_name(self):
    return self.first_name + ' ' + self.last_name	

@login_required(login_url='login')
def habits(request):
	goals = Goals.objects.all()
	context = {'goals':goals}

	return render(request,'accounts/habits.html',context)	

@login_required(login_url='login')
def goals(request,pk):
	
	customer = Customer.objects.get(id=1)
	

	if request.method =='POST':
		form = GoalsForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect('/habits')
	else:
		form = GoalsForm()

	context = {'form':form}

	return render(request,'accounts/goal_form.html',context)

@login_required(login_url='login')
def updateGoals(request, pk):

	goal = Goals.objects.get(id=pk)
	form = GoalsForm(instance=goal)
	
	if request.method == 'POST':
		form = GoalsForm(request.POST, instance=goal)
		if form.is_valid():
			form.save()
			return redirect('/habits')
	else:
		form = GoalsForm()

	context = {'form':form}

	return render(request, 'accounts/goal_form.html', context)

@login_required(login_url='login')
def deleteGoals(request, pk):
	goal = Goals.objects.get(id=pk)
	if request.method == "POST":
		goal.delete()
		return redirect('/habits')
		

	context = {'item':goal}
	return render(request, 'accounts/delete.html', context)