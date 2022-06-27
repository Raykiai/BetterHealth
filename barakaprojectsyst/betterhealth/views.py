from django.forms import CharField
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import RecordInfo
from .models import ChildInfo
from .models import DiagnosisInfo
import joblib

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def register(request):
    return render(request, 'register.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def patients(request):
    return render(request, 'patients.html', {})

def charts(request):
    return render(request, 'charts.html', {})

def form(request):
    return render(request, 'form.html', {})

def childform(request):
    return render(request, 'childform.html', {})

def diagnosis(request):
    return render(request, 'diagnosis.html', {})

def add_record_form_submission(request):
    print("Submitted")
    pid = request.POST.get('pid')
    date = request.POST.get('date')
    fname = request.POST.get('fname')
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    weight = request.POST.get('weight')
    wCategory = request.POST.get('wCategory')
    height = request.POST.get('height')
    hCategory = request.POST.get('hCategory')
   

    record_info = RecordInfo(pid=pid, date=date, fname=fname, age=age, sex=sex, weight=weight, wCategory=wCategory,
                             height=height, hCategory=hCategory,)

    record_info.save()
    return render(request, 'form.html')

def add_patient_form_submission(request):
    print("Submitted")
    dob = request.POST.get('dob')
    fname = request.POST.get('fname')
    sex = request.POST.get('sex')
    cname = request.POST.get('cname')
    phone = request.POST.get('phone')
    residence = request.POST.get('residence')
   

    child_info = ChildInfo(dob=dob, fname=fname, sex=sex, cname=cname, phone=phone, residence=residence,)

    child_info.save()
    return render(request, 'childform.html')

def add_diagnosis_form_submission(request):
    pid = request.POST.get('pid')
    date = request.POST.get('date')
    fname = request.POST.get('fname')
    nid = request.POST.get('nid')
    diagnosis = request.POST.get('diagnosis')
   
    diagnosis_info = DiagnosisInfo(pid=pid, date=date, fname=fname, nid=nid, diagnosis=diagnosis, )

    diagnosis_info.save()
    return render(request, 'diagnosis.html')


def showrecordinfo(request):
	record=RecordInfo.objects.all() # Collect all records from table 
	return render(request,'dashboard.html',{'record':record})

def showdiagnosisinfo(request):
	viewdiagnosis=DiagnosisInfo.objects.all() # Collect all records from table 
	return render(request,'viewdiagnosis.html',{'viewdiagnosis':viewdiagnosis})

def showchildinfo(request):
	child=ChildInfo.objects.all() # Collect all records from table 
	return render(request,'patients.html',{'child':child})

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


def result(request):
    cls = joblib.load('random_forest.sav')

    
    pid = request.POST.get('pid')
    # name = request.POST['name']
    age = request.POST.get('age')
    # sex = request.POST['sex']
    weight = request.POST.get('weight')
    height = request.POST.get('height')

    lis = []
    lis.append(pid)
    # lis.append(name)
    lis.append(age)
    # lis.append(sex)
    lis.append(weight)
    lis.append(height)

    ans = cls.predict([lis])

    return render(request,"result.html", {'ans':ans})
