from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('contact_add', contact_add, name='add')
]