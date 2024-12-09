from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home,name="home"),
    path('signin/',signin,name="signin"),
    path('signup/',signup,name="signup"),
    path('hackathon/',hackathon,name="hackathons"),
    path('questions/',questions,name="questions"),
    path('signin/',signin,name="signin"),
    path('profile/',profile,name="profile"),
    path('discussion/',discussion,name="discussion"),
    path('post/<int:sno>',post,name="post"),
    path('signout/',signout,name="signout"),
    path('search',serach,name="search"),
    path('profileinfo/',profileinfo,name="profileinfo"),
    path('studentinfo/',student_info,name="student_info"),
    path('professionalinfo/',professional_info,name="professional_info"),
    path('project/',project,name="project"),
    path('projectview/<int:sno>',projectview,name="projectview"),
    path('createproject/',createproject,name="createproject"),
    path('viewfile/<int:sno>/<int:foldersno>/',viewfile,name="viewfile"),
    path('projectlist/',projectlist,name="projectlist"),
    path('othersprofile/<str:username>/',othersprofile,name="othersprofile"),
    path('collab/<int:id>/',collab,name="collab")
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)