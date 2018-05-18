from django.db import models
import uuid


#################################################################
# 顧客マスタ
#################################################################
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


#################################################################
# アイテムマスタ
#################################################################
class ItemMaster(models.Model):
    # 商品コード
    item_code = models.CharField(max_length=30, null=False)
    # 商品名
    item_name = models.CharField(max_length=255, null=False)
    # 価格
    price = models.PositiveIntegerField()

    # テーブル名定義
    # sales_historyに変更
    class Meta:
        db_table = 'item_master'


#################################################################
# 売上履歴
#################################################################
class SalesHistory(models.Model):
    # 顧客コード(外部キー)
    customer_code = models.ForeignKey('CustomerMaster', on_delete=models.PROTECT)
    # 商品名コード(外部キー)
    item_master = models.ForeignKey('ItemMaster', on_delete=models.PROTECT)
    # 販売日時
    sold_datetime = models.DateTimeField("販売日時")

    # テーブル名定義
    # sales_historyに変更
    class Meta:
        db_table = 'sales_history'
