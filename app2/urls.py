from django.urls import path
from app2.views import *
app_name='food2'

urlpatterns = [
    path('idli/',idli,name='idli'),
]
