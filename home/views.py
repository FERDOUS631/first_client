from django.shortcuts import render
from .models import *   

# Create your views here.
def home(request):
    profile_data= profile.objects.first()
    about_data= about.objects.first()
    skills_data= Skill.objects.all()
    logo_data= logo.objects.first()
    resume_data= resume.objects.first()
 
    context={
        'profile':profile_data,
        'about':about_data,
        'skills':skills_data,
        'logo':logo_data,
        'resume':resume_data,
        
    }


    return render(request, 'index.html', context)