from django.shortcuts import render, redirect
# Create your views here.

from .forms import ProfessorInfoForm
from .models import Professor
from home.utilities import get_or_create_default_faculty
from django.contrib.auth.hashers import make_password
import logging
logging.basicConfig(level=logging.NOTSET)

from home.forms import AddressForm
from home.models import Address

def register(request):
    try:
        if request.method == "GET":
            professorForm = ProfessorInfoForm(prefix="professor-info")
            professorAddressForm = AddressForm(prefix="professor-address")
        elif request.method == "POST":
            professorForm = ProfessorInfoForm(request.POST, files=request.FILES, prefix="professor-info")
            professorAddressForm = AddressForm(request.POST, prefix="professor-address")
            f1 = professorAddressForm.is_valid()
            f2 = professorForm.is_valid()
            if f1:
                data = professorAddressForm.cleaned_data
                professorAddress, _ = Address.objects.get_or_create(**data)
                if f2:
                    data = professorForm.cleaned_data | dict(address=professorAddress)
                    data['password'] = make_password(data['password'])
                    professor, _ = Professor.objects.get_or_create(**data)
                    faculty = get_or_create_default_faculty()
                    if faculty not in professor.faculties.all():
                        professor.faculties.add(faculty)
                    return redirect('professor-profile', username=professor.username)
        else:
            raise Exception(f"[Professor-Register]: Unknown method {request.method}!")
        return render(request, 'professors/register.html', {
            'professorForm': professorForm,
            'professorAddressForm': professorAddressForm
        })
    except Exception as e:
        logging.debug(e)
        return redirect('error-page')

def profile(request, username):
    try:
        professor = Professor.objects.get(username=username)
        if professor:
            logging.debug(professor.as_data())
            logging.debug(list(professor.faculties.all()))
            return render(request, 'professors/profile.html', {
                'professor': professor,
                'professor_dict': professor.as_data()
            })
        raise Exception("Professor not found!")
    except Exception as e:
        logging.debug(e)
        return redirect('error-page')