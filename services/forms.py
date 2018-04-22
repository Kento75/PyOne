from django.forms import ModelForm, TextInput
from services.models import CustomerMaster


class CustomerForm(ModelForm):
    class Meta:
        model = CustomerMaster
        fields = (
            'customer_name',
            'address',
            'phone_number',
            'mail',
        )

        labels = {
            'customer_name': '顧客名',
            'address':       '住所',
            'phone_number':  '電話番号(ハイフン無)',
            'mail':          'メールアドレス',
        }

        widgets = {
            'customer_name': TextInput(attrs={'class': 'form-control'}),
            'address':       TextInput(attrs={'class': 'form-control'}),
            'phone_number':  TextInput(attrs={'class': 'form-control'}),
            'mail':          TextInput(attrs={'class': 'form-control'}),
        }
