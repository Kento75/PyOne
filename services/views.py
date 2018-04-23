from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from services.models import *
from services.forms import CustomerForm


class CustomerList(ListView):
    model = CustomerMaster
    template_name = "services/customer_list.html"
    paginate_by = 10  # 1ページあたりに表示する件数


class CustomerCreate(CreateView):
    model = CustomerMaster
    form_class = CustomerForm
    template_name = 'services/customer_add.html'
    success_url = reverse_lazy('services:customer_list')


class CustomerUpdate(UpdateView):
    model = CustomerMaster
    form_class = CustomerForm
    template_name = 'services/customer_update.html'
    success_url = reverse_lazy('services:customer_list')
