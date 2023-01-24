from django.shortcuts import render, redirect
# Create your views here.

from .forms import RegistrationForm
from .models import Professor

def register(request):
    try:
        if request.method == "GET":
            registration_form = RegistrationForm()
        elif request.method == "POST":
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                registration_form.save()
                print(registration_form.cleaned_data)
                return redirect('professor-profile', username=registration_form.cleaned_data['username'])
        else:
            raise Exception(f"[Professor-Register]: Unknown method {request.method}!")
        return render(request, 'professors/register.html', {
            'form': registration_form
        })
    except Exception as e:
        print(e)
        return redirect('error-page')

def profile(request, username):
    try:
        professor = Professor.objects.get(username=username)
        if professor:
            return render(request, 'professors/profile.html', {
                'professor': professor
            })
        raise Exception("Professor not found!")
    except Exception as e:
        print(e)
        return redirect('error-page')