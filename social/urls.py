from django.urls import path
from .import views

urlpatterns=[
          path('',views.list_thing,name="home_page"),
          path('list_retrieve/<str:pk>/',views.listthing_retrieve,name="listthing_retrieve"),
          path('listcreate/',views.list_create,name="list_createpage"),
          path('listupdate/<str:pk>/',views.list_update,name="list_updatepage"),
]