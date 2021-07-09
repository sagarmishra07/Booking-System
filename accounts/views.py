from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from Book import models
# Create your views here.

def login(request):
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		msg = None
		user = auth.authenticate(username=username, password=password)

		if user is None:
			return redirect("/account/login")
		
		if user.is_authenticated and user.is_superuser == False:
			auth.login(request, user)
			return redirect("/book")
		
		elif user.is_superuser == True:
			
			auth.login(request, user)
			return redirect("/admin")
		else:
			
			return redirect("/account/login")	
	
	return render(request, 'login.html')



def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		
		username = request.POST['username']
		password = request.POST['password']
		
		email = request.POST['email']

		
		user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
		user.save()
		
		return redirect('/')
	return render(request, 'register.html')


def logout(request):
	auth.logout(request)
	return redirect('/')
