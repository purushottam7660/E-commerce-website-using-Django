from django import forms
from django.contrib.auth.models import User
from accounts.models import Userdetails
from products.models import Products,Category
# from django_recaptcha.fields import ReCaptchaField


class userForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    # user_img = forms.ImageField(label='Profile Image', required=False)

    class Meta:
        model=User
        # fields='__all__'
        fields=['username','password','email']

class userprofileForm(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = ['user_img','phone', 'address', 'street', 'landmark', 'city', 'state', 'zipcode']
        

class Product_Form(forms.ModelForm):
    class Meta:
        model = Products
        fields=['categorys_m','Products_name','prod_img','price','P_description']

class Category_Form(forms.ModelForm):
    class Meta:
        model = Category
        fields='__all__'



