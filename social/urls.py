from django.urls import path
from .import views

urlpatterns=[
    path('',views.homepage,name="homepage"),
    path('detail/<str:pk>/',views.photodetailpage,name="detailpage"),
    
]