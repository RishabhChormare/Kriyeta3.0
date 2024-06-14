from django.shortcuts import render

# Create your views here.  
def index(request):
    return render(request, 'index.html')

def doctor_nurse(request):
    return render(request, 'doctor_nurse.html')

def admin(request):
    return render(request, 'admin.html')

def about(request):
    return render(request, 'about.html')