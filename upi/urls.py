from django.contrib import admin
from django.urls import path
from upi.views import home,success

urlpatterns=[
    path('',home,name='home'),
    path('success',success,name='success')

]