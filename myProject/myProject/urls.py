
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',homePage,name='homePage'),
    path('loginPage/',loginPage,name='loginPage'),
    path('signupPage/',signupPage,name='signupPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('addskillPage/',addskillPage,name='addskillPage'),
    path('addEducation/',addEducation,name='addEducation'),
    path('addInterest/',addInterest,name='addInterest'),
    path('addLanguage/',addLanguage,name='addLanguage'),
    path('createResume/',createResume,name='createResume'),
    path('createResume/',createResume,name='createResume'),
    path('profilePage/',profilePage,name='profilePage'),
    path('addLanguage/',addLanguage,name='addLanguage'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
