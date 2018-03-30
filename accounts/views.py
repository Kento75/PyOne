from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.views.generic import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


'''
@method_decorator(login_required, name='dispatch')
デコレータを使用してクラス実装をする
'''


@python_2_unicode_compatible
class Index(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'home/home.html')
