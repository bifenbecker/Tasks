from django.urls import path, include
from .views import *


urlpatterns = [
    path('', MainPageView.as_view(), name='donationalerts_url'),
    path('login/', LoginView.as_view(), name='login_url'),
]