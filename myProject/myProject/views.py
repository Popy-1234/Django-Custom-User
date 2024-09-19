from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def homePage(req):
    return render(req,'homePage.html')

def loginPage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            login(req,user)
            return redirect('homePage')
          
    return render(req,'loginPage.html')

def signupPage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        usertype=req.POST.get('usertype')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')

        if password == confirm_password:
            user=CustomUser.objects.create_user(
                username=username,
                email=email,
                usertype=usertype,
                password=password,
               
            )
            return redirect('loginPage')
    return render(req,'signupPage.html')

def logoutPage(req):
    logout(req)
    return redirect('loginPage')

def addskillPage(req):
    if req.user.usertype == 'admin':
        return render(req,'addskillPage.html')
    else:
        return HttpResponse('You are not authoirzed to access this page')

def addEducation(req):
    if req.user.usertype == 'admin':
        return render(req,'addEducation.html')
    else:
        return HttpResponse('You are not authoirzed to access this page')

def addInterest(req):
    return render(req,'addInterest.html')

def addLanguage(req):
    if req.user.usertype == 'viewer':
        return render(req,'addLanguage.html')
    else:
        return HttpResponse('You are not authoirzed to access this page')

def createResume(req):
    if req.user.usertype == 'viewer':
        current_user=req.user

        if req.method=='POST':

            resume, created=ResumeModel.objects.get_or_create(user=current_user)

            resume.designation=req.POST.get('designation'),
            resume.contact_no=req.POST.get('contact_no'),
            resume.age=req.POST.get('age'),
            resume.gender=req.POST.get('gender'),
            resume.profile_pic=req.FILES.get('profile_pic'),
            resume.carrer_summary=req.POST.get('carrer_summary'),
               
            resume.save()

            current_user.first_name=req.POST.get('first_name')
            current_user.last_name=req.POST.get('last_name')

            current_user.save()
        return render(req,'createResume.html')
    else:
        return HttpResponse('You are not authoirzed to access this page')
    

def profilePage(req):
    current_user=req.user

    information=get_object_or_404(ResumeModel,user=current_user)
    Language=LanguageModel.objects.filter(user=current_user)

    context={
        'Information':information,
        'Language':Language
    }

    return render(req,'profilePage.html',context)

def addLanguage(req):
    if req.user.usertype == 'viewer':
        current_user=req.user
        if req.method=='POST':

            resume=LanguageModel(
                user=current_user,
                language_name=req.POST.get('language_name')
            )
            resume.save()
    return render(req,'profilePage.html')