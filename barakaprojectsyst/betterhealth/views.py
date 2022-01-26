from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import RecordInfo

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def register(request):
    return render(request, 'register.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def charts(request):
    return render(request, 'charts.html', {})

def form(request):
    return render(request, 'form.html', {})

def add_record_form_submission(request):
    print("Submitted")
    
    date = request.POST['date']
    fname = request.POST['fname']
    age = request.POST['sex']
    weight = request.POST['weight']
    wCategory = request.POST['wCategory']
    height = request.POST['height']
    hCategory = request.POST['hCategory']
    bFeeding = request.POST['bFeeding']
    suppliment = request.POST['suppliment']
    development = request.POST['development']

    record_info = RecordInfo(date=date, fname=fname, age=age, weight=weight, wCategory=wCategory,
                             height=height, hCategory=hCategory, bFeeding=bFeeding, suppliment=suppliment, development=development,)

    record_info.save()
    return render(request, 'form.html')


def my_view(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # login(request, user)
                # Redirect to a success page.
                return redirect('home.html')
        
        else:
            messages.error(request, 'username or password not correct')
            return redirect('login.html')
