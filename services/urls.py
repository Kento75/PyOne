from django.urls import path
from services.views import (
    CustomerList,
    CustomerAdd,
    CustomerEdit,
    CustomerDelete,
)
from django.contrib.auth.decorators import login_required


app_name = 'services'

urlpatterns = [
    path('list/', login_required(CustomerList.as_view()), name='customer_list'),        # 一覧画面へ遷移
    path('add/', login_required(CustomerAdd.as_view()), name='customer_add'),           # 新規登録画面へ遷移
    path('edit/<pk>/', login_required(CustomerEdit.as_view()), name='customer_edit'),   # 更新画面へ遷移
    path(r'delete/<pk>/', login_required(CustomerDelete.as_view()), name='customer_delete'),     # 削除実行
]
