from django.urls import path
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from .views import Index, PasswordChange, PasswordChangeDone

app_name = 'accounts'

urlpatterns = [
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),     # ログイン画面へ遷移
    path('logout/', logout, {'template_name': 'accounts/login.html'}, name='logout'),  # ログアウト→ログイン画面へ遷移
    path('index/', Index.as_view(), name='account_index'),                             # ログイン→ホーム画面へ遷移
    path('password_change/',
         login_required(PasswordChange.as_view()), name='password_change'),            # パスワード変更画面へ遷移
    path('password_change/done/',
         login_required(PasswordChangeDone.as_view()), name='password_change_done'),   # パスワード変更後画面へ遷移
]
