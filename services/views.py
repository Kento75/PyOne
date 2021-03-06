from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from services.models import *
from services.forms import CustomerForm


# 【顧客管理】リスト一覧画面
class CustomerList(ListView):
    model = CustomerMaster
    template_name = "services/customer/customer_list.html"
    paginate_by = 10  # 1ページあたりに表示する件数


# 【顧客管理】リスト一覧画面
class CustomerDetailView(DetailView):
    """
    1つのメモを詳細表示
    テンプレートは、何も指定しないと モデル名_detail.html が使われる
    """
    model = CustomerMaster


# 【顧客管理】新規登録画面
class CustomerAdd(CreateView):
    model = CustomerMaster
    form_class = CustomerForm
    template_name = 'services/customer/customer_add.html'
    success_url = reverse_lazy('services:customer_list')


# 【顧客管理】更新画面
class CustomerEdit(UpdateView):
    model = CustomerMaster
    form_class = CustomerForm
    template_name = 'services/customer/customer_edit.html'
    success_url = reverse_lazy('services:customer_list')


# 【顧客管理】削除画面
class CustomerDelete(DeleteView):
    model = CustomerMaster
    form_class = CustomerForm
    template_name = 'services/customer/customer_delete.html'
    success_url = reverse_lazy('services:customer_list')
