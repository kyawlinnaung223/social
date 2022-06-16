from django.shortcuts import render,redirect


#home pageview
def homepage(request):
    return render(request,'home.html')
#end homepageview


