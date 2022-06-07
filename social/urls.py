from django.urls import path
from .import views

urlpatterns=[
          path('',views.list_thing,name="home_page"),
          path('list_retrieve/<str:pk>/',views.listthing_retrieve,name="listthing_retrieve"),
          path('list_crate/',views.list_create,name="list_createpage"),
]