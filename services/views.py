from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from services.models import *
from services.forms import CustomerForm


class CustomerList(ListView):
    model = CustomerMaster
    template_name = "services/customer_list.html"
    paginate_by = 10


class CustomerCreate(CreateView):
    model = CustomerMaster
    form_class = CustomerForm
    template_name = 'services/customer_create.html'
    success_url = reverse_lazy('services:principal')


class CustomerUpdate(UpdateView):
    model = CustomerMaster
    form_class = CustomerForm
    template_name = 'services/customer_update.html'
    success_url = reverse_lazy('services:principal')
