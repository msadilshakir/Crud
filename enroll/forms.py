from django import forms
from .models import User


class Student_registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
    def clean_name(self):  # Validates the Computer Name Field
        name = self.cleaned_data.get('name')
        if (name == ""):
            raise forms.ValidationError('This field cannot be left blank')
        for instance in User.objects.all():
            if instance.name == name:
                raise forms.ValidationError('Name Already Exist')
        return name 
    def clean_email(self):  # Validates the Computer Name Field
        email = self.cleaned_data.get('email')
        if (email == ""):
            raise forms.ValidationError('This field cannot be left blank')
        for instance in User.objects.all():
            if instance.email == email:
                raise forms.ValidationError('Email Already Exist')
        return email 

class Student_registrationupdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

