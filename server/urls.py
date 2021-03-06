
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.views.generic import TemplateView
from homepage import urls as api_urls
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'server/',include('wxapp.urls')),
    url(r'api/',include(api_urls)), 
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/img/favicon.ico')),  
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
