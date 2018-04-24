from django.db import models
import uuid


class CustomerMaster(models.Model):
    customer_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=255, null=True)
    mail = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'customer_master'

    def __str__(self):
        return self.customer_code
