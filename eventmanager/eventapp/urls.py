from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('schedule', views.schedule, name="schedule"),
    path('speakers', views.speakers, name="speakers"),
    path('register', views.register, name="register"),
    path('contact', views.contact, name="contact"),
]