"""
URL configuration for recipies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('upload/',upload,name='home'),
    path('home/',home,name='home'),
    path('login/',login_page,name='home'),
    path('marks/<id>/',see_marks,name='home'),


    path('student/',get_st,name='home'),

    path('register/',register,name='home'),
    path('logout/',logout_page,name='home'),

    path('del_rcp/<id>/',del_rcp,name='del_rcp'),
    path('upd_rcp/<id>/',upd_rcp,name='upd_rcp'),
    # path('next/<pg>/',next_pg,name='home')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)
    
urlpatterns+= staticfiles_urlpatterns()