from django.urls import path
from services.views import CustomerList, CustomerCreate, CustomerUpdate

app_name = 'services'

urlpatterns = [
    path('list/', CustomerList.as_view(), name="customer"),
    path('clear/', CustomerCreate.as_view(), name="clear"),
    path('edit/<customer_code>/', CustomerUpdate.as_view(), name='edit'),
]
