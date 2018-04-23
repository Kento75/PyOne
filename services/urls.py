from django.urls import path
from accounts.models import AuthUser
from services.views import CustomerList, CustomerCreate, CustomerUpdate
from django.contrib.auth.decorators import login_required


app_name = 'services'

urlpatterns = [
    path('list/', login_required(CustomerList.as_view()), name='customer_list'),
    path('add/', login_required(CustomerCreate.as_view()), name='customer_add'),
#    path('edit/<customer_code>/', CustomerUpdate.as_view(model = AuthUser), name='customer_edit'),
]
