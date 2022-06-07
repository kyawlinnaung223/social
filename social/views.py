from django.shortcuts import render


# Create your views here.
#start homepageview
def homepageviewpage(request):
          return render(request,'home.html')
#end homepageview
