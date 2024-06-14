from django.shortcuts import render,get_object_or_404


def index (request):
    return render (request , "HTML/index.html")


def about (request):
    return render (request , "HTML/about.html")

def contact (request):
    return render (request , "HTML/contact.html")

def login (request):
    return render (request , "HTML/login.html")

def register (request):
    return render (request , "HTML/register.html")

def services (request):
    return render (request , "HTML/services.html")

def admin (request):
    return render (request , "HTML/admin.html")

def doctor_nurse (request):
     return render (request , "HTML/doctor_nurse.html")

# def model (request):
#     return render (request , "HTML/TrainedModel.html")

# def read(request):
#     return render(request, "HTML/recieve.html")