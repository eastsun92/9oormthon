"""
URL configuration for goormthon_app project.

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
from .views import GPTPromptView, JejuTouristSpotList
from django.views.generic import TemplateView

urlpatterns = [
    path('gpt-prompt/', GPTPromptView.as_view(), name='gpt-prompt'),
    path('', TemplateView.as_view(template_name='gpt_prompt_test.html'), name='home'),  # 루트 URL
    path('admin/', admin.site.urls),
    path('api/jeju-tourist-spots/', JejuTouristSpotList.as_view(), name='jeju-tourist-spots'),
]
