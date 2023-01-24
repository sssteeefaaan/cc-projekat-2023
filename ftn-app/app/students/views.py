from django.shortcuts import render, redirect
# Create your views here.

from .forms import RegistrationForm
from .models import Student
import logging

def register(request):
    try:
        logging.basicConfig(level=logging.NOTSET)
        logging.debug("HEY1")
        if request.method == "GET":
            registration_form = RegistrationForm()
        elif request.method == "POST":
            logging.debug("HEY2")
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                logging.debug("HEY3")
                registration_form.save()
                print(registration_form.cleaned_data)
                return redirect('student-profile', username=registration_form.cleaned_data['username'])
            logging.debug(registration_form)
        else:
            raise Exception(f"[Student-Register]: Unknown method {request.method}!")
        return render(request, 'students/register.html', {
            'form': registration_form
        })
    except Exception as e:
        logging.debug(e)
        return redirect('error-page')

def profile(request, username):
    try:
        student = Student.objects.get(username=username)
        if student:
            return render(request, 'students/profile.html', {
                'student': student
            })
        raise Exception("Student not found!")
    except Exception as e:
        print(e)
        return redirect('error-page')