from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
   path("",views.index, name='home'),
   path("about",views.about, name='about'),
   path('output', views.output, name="webcam"),
   path('downloadfile', views.downloadfile, name="downloadfile"),
   path('picked', views.picked, name="picked"),
   path('register_on', views.register_on, name="register_on"),
   path('give_feedback', views.give_feedback, name="give_feedback"),
   path('contact', views.contact, name="contact"),
]