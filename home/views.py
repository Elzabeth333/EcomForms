from django.shortcuts import render, get_object_or_404,redirect
from .models import Products , Category
from .forms import ProductForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User  
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    logged_user = request.user
    product = Products.objects.all()
    return render(request,'home/home.html',{
        'Products':product ,
        'logged_user':logged_user
                                            })

def add_product(request): 
    if request.method == 'POST':
         product_form = ProductForm(request.POST, request.FILES)
         if product_form.is_valid():
             product_form.save()
             messages.success(request,'Successfully added New Product')
             return redirect('home')

    product_form = ProductForm()
    return render(request,'home/add_product.html',{'form': product_form })

def edit_product(request,product_id):
    product = get_object_or_404(Products, id =  product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST , request.FILES ,instance= product)
        if product_form.is_valid():
            product_form.save()
            return redirect('home')

    product_form = ProductForm(instance= product)
    return render(request, 'home/edit_product.html', {'form':product_form})

def delete_product(request,product_id):
    product = get_object_or_404(Products, id =  product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'home/delete_product.html',{'product':product})



def registration(request):  
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Registered successfully')
            return redirect('home')   
    else:
        form = RegistrationForm()     

    
    return render(request,'home/registration.html',{'form':form})

def user_login(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:                    
                    return redirect('admin_home')  
                else:                    
                    return redirect('user_home')    
                         
            else:                
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form': form})

@login_required
def admin_home(request):
    logged_user = request.user
    return render(request,'home/admin_home.html',{'logged_user':logged_user})

@login_required
def user_home(request):
    logged_user = request.user
    return render(request,'home/user_home.html',{'logged_user':logged_user})


def user_logout(request):
    logout(request)   
    return redirect('home')