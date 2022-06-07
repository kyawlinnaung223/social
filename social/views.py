from django.shortcuts import render
from .models import listhing
from .forms import ListFrom

# Create your views here.
#start homepageview
def list_thing(request):
          listthings=listhing.objects.all()
          context={'listthings':listthings}
          return render(request,'home.html',context)
#end homepageview


#start listthing_retrieve
def listthing_retrieve(request, pk):
          listthings=listhing.objects.get(id=pk)
          context={'listthings':listthings}
         
          return render(request,'listing_retrieve.html',context)
#end listthing_retrieve

#start listcreateForm
def list_create(request):
          form=ListFrom()
          context={'form':form}
          return render (request,'list_create.html',context)
#end listcreateForm

