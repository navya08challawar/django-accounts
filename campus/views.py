# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Campus
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django import forms
# Create your views here.

def campus_list(request):
	campus=Campus.objects.all().order_by('date')
	return render(request,'campus/campus_list.html',{'campus':campus})

def campus_details(request,slug):
	try:
		campus = Campus.objects.get(slug=slug)
	except Campus.DoesNotExist:
		campus=None
	return render(request,'campus/campus_detail.html',{'campus':campus})
def signup_view(request):
	if request.method =="POST":
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect('campus:list')
	else:
		form=UserCreationForm()
		return render(request,'accounts/signup.html',{'form':form})
def login_view(request):
	if request.method =="POST":
		form= AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log in the user
			user=form.get_user()
			login(request,user)
			if'next'in request.POST:
				return redirect(request.POST.get('next'))
			return redirect('campus:list')
	
	else:
		form=AuthenticationForm()
		return render(request,'accounts/login.html',{'form':form})
def logout_view(request):
	if request.method=='POST':
		logout(request)
		return redirect('campus:list')
		@login_reqired(login_url="/accounts/login/")

		def campus_create(request):
			if request.method =='POST':
				form=forms.CreateArticle(request.POST,request.FILES)
				if form.is_valid():
					# save articleto db
					instance=form.save(commit=False)
					instance.author=request.user
					instance.save()
					return redirect('articles:list')

			else:
				form=forms.CreateArticle()
	return render(request,'campus/campus_create.html',{'forms':form})		



	

