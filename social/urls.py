from django.urls import path
from .import views

urlpatterns=[
          path('',views.homepageviewpage,name="home_page"),
]