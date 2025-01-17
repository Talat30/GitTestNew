from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import cache_control 

# Create your views here.

from django.shortcuts import render
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
     return render(request,'home.html',{'name':'Talat'})

@login_required(login_url='login')
def add(request):
   val1=int(request.POST['num1'])
   val2=int(request.POST['num2'])
   val3=val1+val2
   return render(request,'result.html',{'result':val3})

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
   return render(request,'dashboard.html')

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def product(request):
      return render(request,'product.html')
from .models import *

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
  customers=Customer.objects.all()
  orders=Order.objects.all()
  return render(request,'dashboard.html',{'customers':customers,'orders':orders})

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def product(request):
  products=Product.objects.all()
  return render(request,'product.html',{'products':products})

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def customer(request, pk):
   customer=Customer.objects.get(id=pk)
   customers=Customer.objects.all()
   orders=customer.order_set.all()
   order_count=orders.count()
   context={'customers':customers, 'cust':customer,'orders':orders,'ordcount':order_count}
   return render(request,'customer.html',context)
from .forms import OrderForm
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def createOrder(request):
    form=OrderForm()
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request,'order_form.html',context)
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateOrder(request, pk):

    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=="POST":
        form=OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'order_form.html',context)

@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deleteOrder(request, pk): 
    order=Order.objects.get(id=pk) 
    if request.method=="POST": 
        order.delete() 
        return redirect('/') 
    context={'item':order}
    return render(request,'delete.html',context)

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def registerPage(request): 
    #form=UserCreationForm() 
    form=CreateUserForm() 
    if request.method=="POST": 
        form=UserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('login') 
        else: 
            messages.success(request,"Password does not follow the rules") 
            
    context={'form':form} 
    return render(request, 'register.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loginPage(request): 
    if request.user.is_authenticated: 
        return redirect('home') 
    else: 
        if request.method=='POST': 
            username=request.POST.get('username') 
            password=request.POST.get('password') 
            print(username, password) 
            user = authenticate(request, username=username, password=password) 
            if user is not None: 
                login(request, user) 
                return redirect('home') 
            else: 
                messages.success(request,"Username or Password is incorrect") 
        context={} 
        return render(request,'login.html',context)
@login_required(login_url='login') 
@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def logoutPage(request): 
    logout(request) 
    return redirect('login') 

from .forms import CreateUserForm

def insertData(request):
    n=request.POST['nameVar']
    a=request.POST['ageVar']
    Customer.objects.create(name=n, age=a);
    customers=Customer.objects.all()
    return render(request,'home.html',{'customers':customers})

