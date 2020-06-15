from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.contrib.auth.models import User
from Login_App.models import UserProfile

class SignUp(UserCreationForm):
    email = forms.EmailField(label="Email Adress",required=True)
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
class UserChange(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name' ,'password')
class ProfilePic(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields=['ProfilePic']
