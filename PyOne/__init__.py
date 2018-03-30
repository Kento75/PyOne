from django.utils.translation import ugettext_lazy
from django.contrib import admin


# admin画面カスタマイズ
# タイトル等の変更
admin.site.site_title = ugettext_lazy('PyOne管理画面')
admin.site.site_header = ugettext_lazy('PyOne管理画面')
admin.site.index_title = ugettext_lazy('')
