"""hknweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include
from django.urls import path

from .views import landing
from .views import users

urlpatterns = [
    path('', landing.home),
    path('admin/', admin.site.urls),
    path(
        'accounts/', include([
            path('profile/', users.account_settings),
            path('settings/', users.account_settings),
            path('login/', auth_views.LoginView.as_view(template_name='admin/login.html')),
            path('logout/', auth_views.LogoutView.as_view()),
        ]),
    ),
    path('events/', include('hknweb.events.urls')),
    path('alumni/', include('hknweb.alumni.urls')),
    path('tutoring/', include('hknweb.tutoring.urls')),
    path('pages/', include('hknweb.markdown_pages.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('s/', include('hknweb.shortlinks.urls')),
    path('elections/', include('hknweb.elections.urls')),
]
