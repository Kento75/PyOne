from django.urls import path
from django.contrib.auth.views import login, logout
from .views import Index

app_name = 'accounts'

urlpatterns = [
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),      # ログイン画面へ遷移
    path('logout/', logout, {'template_name': 'accounts/login.html'}, name='logout'),   # ログアウト→ログイン画面へ遷移
    path('index/', Index.as_view(), name='account_index'),                              # ログイン→ホーム画面遷移
#    path('change_password/', change_password, name='change_password'),
]
