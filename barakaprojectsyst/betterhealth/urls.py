from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('', views.home, name='home'),
   
    path('register/', views.register, name='register'),
    path('dashboard/', views.showrecordinfo, name='dashboard'),
    path('patients/', views.showchildinfo, name='patients'),
    path('viewdiagnosis/', views.showdiagnosisinfo, name='viewdiagnosis'),
    path('charts/', views.charts, name='charts'),
    path('result/', views.result, name='result'),
    path('form/', views.form, name='form'),
    path('childform/', views.childform, name='childform'),
    path('diagnosis/', views.diagnosis, name='diagnosis'),
    path('showrecordinfo/', views.showrecordinfo, name='showrecordinfo'),
    path('add_record_form_submission/', views.add_record_form_submission, name='add_record_form_submission'),
    path('add_diagnosis_form_submission/', views.add_diagnosis_form_submission, name='add_diagnosis_form_submission'),
    path('add_patient_form_submission/', views.add_patient_form_submission, name='add_patient_form_submission'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
]
 