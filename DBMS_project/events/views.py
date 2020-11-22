from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def sports(request):
    return render(request,'sports.html')

def clubs(request):
    return render(request,'clubs.html')

def cultural(request):
    return render(request,'cultural.html')

def department(request):
    return render(request,'department.html')

def equinox1(request):
    return render(request,'equinox1.html')
