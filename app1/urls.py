from django.urls import path
from app1.views import *
app_name='food1'

urlpatterns = [
    path('dosa/',dosa,name='dosa'),
]
