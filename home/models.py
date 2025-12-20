from django.db import models

# Create your models here.

class profile(models.Model):
    profile_image=models.ImageField(upload_to='image/profile/')
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    my_projects=models.IntegerField()
    work_experience=models.IntegerField()
    awards_won=models.IntegerField()
    cv=models.FileField(upload_to='file/cv/')
    fb_link=models.URLField()
    twitter_link=models.URLField()
    linkedin_link=models.URLField()
    github_link=models.URLField()
    instagram_link=models.URLField()
    email = models.EmailField(default='example@example.com')

    def __str__(self):
        return self.name

class about(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    description_2=models.TextField(default='write here')
    degree=models.CharField(max_length=100)
    based_in=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    availability=models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Skill(models.Model):
    name = models.CharField(max_length=100)
    progress = models.PositiveIntegerField()  

    def __str__(self):
        return f"{self.name} ({self.progress}%)"
    

class logo(models.Model):
    logo_image=models.ImageField(upload_to='image/logo/', null=True, blank=True)
    write_logo=models.CharField(max_length=100)

    def __str__(self):
        return str(self.write_logo)

class resume(models.Model):
    resume_title=models.CharField(max_length=300)
    professional_Journey_title=models.CharField(max_length=300)
    education_title=models.CharField(max_length=300)
    service_title=models.CharField(max_length=300, default='Services')
    portfolio_title=models.CharField(max_length=300, default='Portfolio')
    contact_title=models.CharField(max_length=300, default='Get in Touch')
    def __str__(self):
        return self.resume_title
    

class contactMessage(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
class HeroSection(models.Model):
    name = models.CharField(max_length=100)
    typed_items = models.TextField()   
    def __str__(self):
        return self.name

