# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def index(request):
 	return render(request, "login/index.html")

def register(request):
	pass

def login(request):
	pass