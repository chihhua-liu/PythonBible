"""firstproject URL Configuration

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
from django.contrib import admin
from django.urls import path
from myapp.views import sayhello
from myapp.views import hello2
from myapp.views import hello3
from myapp.views import hello4
from myapp.views import show
from myapp.views import djget
from myapp.views import djpost

urlpatterns = {
    path('admin/', admin.site.urls),

    path('', sayhello),  # path(網址, 函式)

    path('hello2/<str:username>', hello2),  # path(網址, 函式)

    path('hello3/<str:username>', hello3),

    path('hello4/<str:username>', hello4),

    path('show', show),

    path('djget', djget),

    path('djpost', djpost),
}
