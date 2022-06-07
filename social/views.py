from django.shortcuts import render,redirect
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
           
          if request.method == 'POST':
                    form=ListFrom(request.POST)
                    if form.is_valid():
                              form.save()
                              return redirect('home_page')
          context={'form':form}
          return render (request,'list_create.html',context)
#end listcreateForm



#start updatelist
def list_update(request,pk):
          listthings=listhing.objects.get(id=pk)
          form=ListFrom(instance=listthings)
          if request.method == 'POST':
                    form=ListFrom(request.POST,instance=listthings)
                    if form.is_valid():
                              form.save()
                              return redirect('home_page')
          context={'form':form}
          return render (request,'list_update.html',context)
          
#end updatelist

