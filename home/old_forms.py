from django import forms
from .models import Category, Product 

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Product Name")
    description = forms.CharField(widget=forms.Textarea, label='Features')
    image = forms.ImageField(label= 'product Image')
    price = forms.DecimalField(max_digits=8,decimal_places=2)
    stock = forms.IntegerField(label='Stock available')
    category = forms.ModelChoiceField(queryset= Category.objects.all(), label='Category')