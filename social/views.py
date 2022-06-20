from django.shortcuts import render,redirect
from .models import*
from django.db.models import Q



#home pageview
def homepage(request):
    photoes=listhing.objects.filter(
        Q(title='Travel On Free Time')|
        Q(title='Enjoy go trip on holiday')|
        Q(title='Trip For Holiday')|
        Q(title='Climb Mounatin')
        
        
        
    )

    explores=listhing.objects.filter(
        Q(title='Explore The World')
    )

    tours=listhing.objects.filter(
        Q(title='Tours Photo')

    )
   
    context={'photoes':photoes,'explores':explores,'tours':tours}

    return render(request,'home.html',context)
#end homepageview


#start photodetail pageview
def photodetailpage(request, pk):
    photoes=listhing.objects.get(id=pk)
    explores=listhing.objects.get(id=pk)
    context={'photoes':photoes,'explores':explores}
    return render(request,'photo-detail.html',context)
#end start photodetail pageview


