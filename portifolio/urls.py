"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views
from .pdf import pdf

app_name = 'portifolio'

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    path('create/personaldata/', views.createpersonaldata,
         name='createpersonaldata'),
    path('edit/personaldata/',
         views.editpersonaldata, name='editpersonaldata'),

    path('views/pdf/', pdf, name='pdf'),

    path('create/socialmedia/', views.createsocialmedia,
         name='createsocialmedia'),
    path('edit/socialmedia/',
         views.editsocialmedia, name='editsocialmedia'),

    path('delete/minicard/<int:minicard_id>/',
         views.deleteminicard, name='deleteminicard'),

    path('create/about/', views.createabout, name='createabout'),
    path('edit/about/',
         views.editabout, name='editabout'),

    path('create/barprogress/', views.createbarprogress,
         name='createbarprogress'),
    path('edit/barprogress/',
         views.editbarprogress, name='editbarprogress'),
    path('delete/barprogress/<int:barprogress_id>/',
         views.deletebarprogress, name='deletebarprogress'),

    path('create/skills/', views.createskills, name='createskills'),
    path('edit/skills/',
         views.editskills, name='editskills'),

    path('create/cards/', views.createcards, name='createcards'),
    path('edit/card/',
         views.editcard, name='editcard'),
    path('delete/card/', views.deletecard, name='deletecard'),

    path('send/email/', views.sendemail, name='sendemail'),
]
