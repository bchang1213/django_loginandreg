# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
 	return render(request, "login/index.html")

def gosignin(request):
	return render(request, "login/signin.html")

def login(request):
	errors = User.objects.login_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
			return redirect('/')
	else:
		user = User.objects.get(email=request.POST['email'])
		if user:
			if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
				messages.error(request, 'Account with those credentials could not be found.')
				return redirect('/')
			else:
				messages.success(request, 'Login Successful!')
				return redirect(reverse('success',kwargs ={'user_id':user.id}))


def goregister(request):
	return render(request, "login/register.html")

def register(request):
	errors = User.objects.basic_validator(request.POST)
	if len(errors):
		for tag, error in errors.iteritems():
			messages.error(request, error, extra_tags=tag)
			return redirect('/')
	else:
		user = User.objects.create()
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email =request.POST['email']
		# user.dob =request.POST['dob']
		user.password =bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		user.save()
		messages.success(request, 'User created. Please login!')
		return redirect('/')

def success(request, user_id):
	context = {
	"user": User.objects.get(id = user_id)
	}
	return	render(request, "login/success.html", context)