from django.forms import ModelForm
from .models import Order
class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
from django import forms  
from django.contrib.auth.models import User 
class CreateUserForm(UserCreationForm): 
    class Meta: 
        model=User 
        fields=["username","email","password1","password2"]

