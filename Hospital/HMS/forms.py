from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Patient,Doctor

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['phone','address']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization','phone','address']