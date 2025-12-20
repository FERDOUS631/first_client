from urllib import request
from django.shortcuts import render
from .models import *   

# Create your views here.
def home(request):
    profile_data= profile.objects.first()
    about_data= about.objects.first()
    skills_data= Skill.objects.all()
    logo_data= logo.objects.first()
    resume_data= resume.objects.first()
    hero_data = HeroSection.objects.first()
    message_sent = False
    message_error = False
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            if name and email and subject and message:
            
                contact_message = contactMessage(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                message_sent= True
            else:
                message_error = True    
        except:
            message_error = True

        contact_message.save()
        message_sent = True
    else:
        message_sent = False

    context={
        'profile':profile_data,
        'about':about_data,
        'skills':skills_data,
        'logo':logo_data,
        'resume':resume_data,
        'message_sent': message_sent, 
        'message_error': message_error,
        'hero_name':hero_data,
    }


    return render(request, 'index.html', context)