from django.db import models
import uuid


# 顧客マスタ
class CustomerMaster(models.Model):
    # 顧客コード
    customer_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 顧客名
    customer_name = models.CharField(max_length=255, null=False)
    # 住所
    address = models.CharField(max_length=255, null=False)
    # 電話番号
    phone_number = models.CharField(max_length=255, null=True)
    # メールアドレス
    mail = models.CharField(max_length=255, null=True)

    # テーブル名定義
    # customer_masterに変更
    class Meta:
        db_table = 'customer_master'

    def __str__(self):
        return self.customer_code
