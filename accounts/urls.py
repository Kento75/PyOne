from django.urls import path
from django.contrib.auth.views import login, logout
from .views import Index

app_name = 'accounts'

urlpatterns = [
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'accounts/login.html'}, name='logout'),
    path('index/', Index.as_view(), name='account_index'),
#    path('change_password/', change_password, name='change_password'),
]
