from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.views.generic import View
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import PasswordChangeForm


# ホーム画面遷移
@python_2_unicode_compatible
class Index(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'home/home.html')


# パスワード変更画面遷移
class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change.html'


# パスワード変更完了画面遷移
class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
