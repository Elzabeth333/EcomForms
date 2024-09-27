from .models import Category, Products
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
import re


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields ='__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name of Product'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
            'product_image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Price'}),
            'stock':forms.NumberInput(attrs={'class':'form-control','placeholder':'Available Stock'}),
            'category':forms.Select(attrs={'class':'form-control'}),



        }
        

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label="First Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label="Last Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Username"
    )
    password1 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password"
    )
    password2 = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm Password"
    )
    
    class Meta:
        model = User  
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        # Check if password length is at least 8 characters
        if len(password1) < 8:
            self.add_error('password1',"Password must be at least 8 characters long.")
        
        # Check if password contains at least one lowercase letter
        if not re.search(r'[a-z]', password1):
            self.add_error('password1',"Password must contain at least one lowercase letter.")
        
        # Check if password contains at least one uppercase letter or number
        # if not re.search(r'[A-Z]', password1):
        #     self.add_error('password1',"Password must contain at least one uppercase letter.")
        # Check if password contains at least one special character
        # if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
        #     self.add_error("Password must contain at least one special character.")
                
        if not re.search(r'[0-9]', password1):
            self.add_error('password1',"Password must contain at least one  number.")
        
        return password1
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")
        else:
            print("Passwords match or not provided")
        
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password"
    )

