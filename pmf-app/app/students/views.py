from django.shortcuts import render, redirect
# Create your views here.

from .forms import StudentInfoForm, ParentInfoForm
from .models import Student, Parent
from home.utilities import get_or_create_default_faculty
from django.contrib.auth.hashers import make_password
from django.conf import settings
import logging
logging.basicConfig(level=logging.NOTSET)

from home.forms import AddressForm, FacultyForm
from home.models import Address, Faculty

def register(request):
    try:
        if request.method == "GET":
            studentForm = StudentInfoForm(prefix="student-info")
            studentAddressForm = AddressForm(prefix="student-address")
            parentForm = ParentInfoForm(prefix="parent-info")
            parentAddressForm = AddressForm(prefix="parent-address")
        elif request.method == "POST":
            studentForm = StudentInfoForm(request.POST, files=request.FILES, prefix="student-info")
            studentAddressForm = AddressForm(request.POST, prefix="student-address")
            parentForm = ParentInfoForm(request.POST, prefix="parent-info")
            parentAddressForm = AddressForm(request.POST, prefix="parent-address")
            f1 = studentAddressForm.is_valid()
            f2 = parentAddressForm.is_valid()
            f3 = parentForm.is_valid()
            f4 = studentForm.is_valid()
            if f1:
                data = studentAddressForm.cleaned_data
                studentAddress, _ = Address.objects.get_or_create(**data)
                if f2:
                    data = parentAddressForm.cleaned_data
                    parentAddress, _ = Address.objects.get_or_create(**data)
                    if f3:
                        data = parentForm.cleaned_data | dict(address=parentAddress)
                        parent, _ = Parent.objects.get_or_create(**data)
                        if f4:
                            data = studentForm.cleaned_data | dict(faculty=get_or_create_default_faculty(), address=studentAddress, parent=parent)
                            data['password'] = make_password(data['password'])
                            student = Student.objects.create(**data)
                            return redirect('student-profile', username=student.username)
        else:
            raise Exception(f"[Student-Register]: Unknown method {request.method}!")
        return render(request, 'students/register.html', {
            'studentForm': studentForm,
            'studentAddressForm': studentAddressForm,
            'parentForm': parentForm,
            'parentAddressForm': parentAddressForm
        })
    except Exception as e:
        logging.debug(e)
        return redirect('error-page')

def profile(request, username):
    try:
        student = Student.objects.get(username=username)
        if student:
            return render(request, 'students/profile.html', {
                'student': student,
                'student_dict': student.as_data()
            })
        raise Exception("Student not found!")
    except Exception as e:
        logging.debug(e)
        return redirect('error-page')