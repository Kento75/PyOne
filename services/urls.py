from django.urls import path
from accounts.models import AuthUser
from services.views import CustomerList, CustomerAdd, CustomerEdit
from django.contrib.auth.decorators import login_required


app_name = 'services'

urlpatterns = [
    path('list/', login_required(CustomerList.as_view()), name='customer_list'),
    path('add/', login_required(CustomerAdd.as_view()), name='customer_add'),
    path('edit/<pk>/', login_required(CustomerEdit.as_view()), name='customer_edit'),
]
