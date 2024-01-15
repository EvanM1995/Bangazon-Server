from enum import Enum
from django.db import models

class OrderType(Enum):
    MOBILE = 'mobile'
    CAFE = 'cafe'

class PaymentType(Enum):
    CASH = 'cash'
    CHECK = 'check'
    CREDIT = 'credit'
    DEBIT = 'debit'
    MOBILE_PAYMENT = 'mobile_payment'

class Revenue(models.Model):
    order_id = models.IntegerField
    datetime_created = models.DateTimeField
    order_type = OrderType
    payment_total = models.DecimalField
    payment_tip = models.DecimalField
    payment_type = PaymentType
