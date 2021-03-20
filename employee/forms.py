from django import forms
from .models import User
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']

        widgets={
            'name':forms.TextInput( attrs={'class':'form-control','placeholder':"Enter your Name",}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':"Enter your Email"}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control','placeholder':"Enter your Password"}),
        }
