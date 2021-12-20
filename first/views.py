from django.shortcuts import render,redirect
import requests
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse,HttpResponse
import json
from .models import *
from json import dumps
from django.core import serializers
# Create your views here.

#this function shows the home page of website where user can upload files
def home(request):
	return render(request,'home.html')
 
#this function is used to save the uploaded file in dataset
def index(request):
	data = json.loads(request.POST['data'])
	data = Data.objects.create(json_data=data)

	return JsonResponse({"message":"ok","id":data.id})

#this function is used to display all the dataset
def display(request):
	all_data = Data.objects.all()
	for data in all_data:
		for key,value in data.json_data.items():
			print(key,value)
	return render(request,'display.html',{'all_data':all_data})

#this function show the data of a particular dataset
def dataset(request,id):
	# data_id = request.POST.get('try')
	data = Data.objects.get(id = id)
	return render (request,'dataset.html',{'data':data})

#this function delete a particular dataset
def delete_data(request):
	if request.method == 'POST':
		data_id = request.POST.get('try')
		data = Data.objects.get(id = data_id)
		data.delete()

		all_data = Data.objects.all()
		return render(request,'display.html',{'all_data':all_data})

#this function is used to search in a particular dataset for a given key
def search_data(request):
	if request.method == 'POST':
		data_id = request.POST['id']
		key1  = request.POST['key']
		data = Data.objects.get(id = data_id)
		context = {'value':'Not present',
					'key': key1}
		for key,value in data.json_data.items():
			if(key==key1):
				context['value'] = value
				break
		return render (request,'output.html',context)

#this function gets the key whose value we want to change
def edit_data(request):
	if request.method == 'POST':
		data_id = request.POST['id']
		key1  = request.POST['key']
		data = Data.objects.get(id = data_id)
		context = {'value':'Not present',
					'key': key1,
					'data' : data}
		for key,value in data.json_data.items():
			if(key==key1):
				context['value'] = value
				break
		return render (request,'edit.html',context)

#this function changes the value of the particular key
def edit_data1(request):
	if request.method == 'POST':
		data_id = request.POST['id']
		value  = request.POST['value']
		key  = request.POST['key']
		data = Data.objects.get(id = data_id)
		context = {'value':'Not present',
					'key': key}
		data.json_data[key] = value
		data.save()
		return render (request,'dataset.html',{'data':data})