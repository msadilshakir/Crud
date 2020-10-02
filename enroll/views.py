from django.shortcuts import render, HttpResponseRedirect
from .forms import Student_registration, Student_registrationupdate
from .models import User
from django.contrib import messages
from django.db.models import Q
#from django.contrib.auth.models import User, auth
# Create your views here.

# This function will add data and show data.


def add_show(request):
    if request.method == 'POST':
        fm = Student_registration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            messages.error(request, 'Form Submitted!!')
            fm = Student_registration()
    else:
        fm = Student_registration()
    stud = User.objects.all().filter()
    #messages.error(request,'Invalid entry')
    return render(request, 'add_show.html', {'form': fm, 'stu': stud})

# This function will delete data.


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# This function will update/edit data


def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = Student_registrationupdate(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = Student_registration(instance=pi)
    return render(request, 'update_student.html', {'form': fm})

# def show(request):

#    fm = Student_registration()
#    return render(request, 'add_show.html', {'stu':stud})


def hide(request):
    return HttpResponseRedirect('/')


def fetch(request):
    fet = request.GET['q']
    st = User.objects.all().filter(Q(name__contains=fet)|Q(email__contains=fet))
    fm = Student_registration()
    return render(request, 'add_show.html', {'stu': st, 'fet': fet,'form':fm})

def del_conf(request):
    return render(request,'del_conf.html')

def submit(request):
    if request.method == 'POST':
        fm = Student_registration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pwd)
            reg.save()
            messages.error(request, 'Form Submitted!!')
            fm = Student_registration()
    else:
        fm = Student_registration()
    stud = User.objects.all().filter()
    #messages.error(request,'Invalid entry')
    return render(request, 'add_show.html', {'form': fm, 'stu': stud})