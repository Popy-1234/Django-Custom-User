from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer'),
    ]

    usertype=models.CharField(choices=USER,max_length=100,null=True)

    def __str__(self) -> str:
        return f"{self.username}-{self.first_name}-{self.last_name}"
    
class ResumeModel(models.Model):
    Gender=[
        ('male','Male'),
        ('female','Female'),
    ]

    user=models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    designation=models.CharField(max_length=100,null=True)
    contact_no=models.CharField(max_length=100,null=True)
    age=models.PositiveIntegerField(null=True)
    gender=models.CharField(choices=Gender,max_length=100,null=True)
    profile_pic=models.ImageField(upload_to="Media/profile_pic",null=True)
    carrer_summary=models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return self.user.username+" "+self.designation

class LanguageModel(models.Model):
  
    user=models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    language_name=models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return self.user.username+" "+self.language_name
