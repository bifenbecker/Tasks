from django.urls import path
from .views import *


urlpatterns = [
    path('', MainAppView.as_view(), name='mainapp_url'),
    path('api/', MainAppAPI.as_view(), name='api_url'),
]