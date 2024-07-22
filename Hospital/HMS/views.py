from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm, PatientForm, DoctorForm
from .models import User

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            if 'is_patient' in request.POST:
                user.is_patient = True
                user.save()
                patient_form = PatientForm(request.POST, instance=user.patient)
                if patient_form.is_valid():
                    patient_form.save()
            elif 'is_doctor' in request.POST:
                user.is_doctor = True
                user.save()
                doctor_form = DoctorForm(request.POST, instance=user.doctor)
                if doctor_form.is_valid():
                    doctor_form.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        patient_form = PatientForm()
        doctor_form = DoctorForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'patient_form': patient_form,
        'doctor_form': doctor_form
    })

def home(request):
    return render(request, 'home.html')
