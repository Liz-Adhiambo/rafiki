
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
# test two


def index(request):
    return render(request, 'landing.html')

def services(request):
    return render(request, 'services.html')

def profile(request):
     profiles = Profile.get_all_profiles()
     return render(request, 'employers/employer.html', {"profiles":profiles})
    

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'

            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_employer:
                login(request, user)
                return redirect('employer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


@login_required(login_url='index')
def logout(request):
    auth.logout(request)
    return redirect('index')


def employer(request):
    profiles = Profile.get_all_profiles()
    return render(request,'employers/employer.html',{"profiles":profiles})



def employee(request):
    
    return render(request,'employees/employee.html')

def update_profile(request):
    Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.instance.user=request.user
            p_form.save()

            messages.success(request, f'Your account has been updated!')
            return redirect('employee')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'employees/update_profile.html', context)    

def public_profile(request, username):  
    obj = User.objects.get(username=username)  

    context = {
        'username': obj,  # obj is now accesible in the html via the variable {{ username }}
        
    }
   
    return render(request, 'employees/public_employee.html',  {'username': obj})



def search_profile(request):
    title = 'Search'
    categories = Category.objects.all()
    if 'profile_category' in request.GET and request.GET['profile_category']:
        search_term = request.GET.get('profile_category')
        found_results = Profile.search_by_category(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {'title':title,'profile': found_results, 'message': message, 'categories': categories})
    else:
        message = 'You havent searched yet'
        return render(request, 'search.html',{"message": message})
