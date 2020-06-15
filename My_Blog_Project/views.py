from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.urls import  reverse
def index(request):
    return HttpResponseRedirect(reverse('Blog_App:blog_list'))
