"""chatbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http import HttpResponse

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

def response(request, slug=None):
    return HttpResponse("""<h1>Welcome</h1>""")

def responseAbout(request, slug=None):
    return HttpResponse("""
                        <h1>Welcome, my name is...</h1>
                        <p>OvO</>
                        """)
from backend import views as backend_views
from frontend import views as frontend_views

urlpatterns = [
    path("", frontend_views.frontend),
    path("about/", responseAbout),
    path("server/", backend_views.backend),
    path("server/get_chat_response", backend_views.get_chat_response),
    path("server/get_first_message", backend_views.get_first_response)    
]

