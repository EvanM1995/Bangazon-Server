from enum import Enum
from django.db import models
from .users import Users

class OrderStatus(Enum):
    OPEN = 'open'
    CLOSED = 'closed'

class Orders(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    customer_email = models.CharField
    customer_name = models.CharField(max_length=25)
    customer_phone = models.CharField
    datetime_created = models.DateTimeField
    datetime_deleted = models.DateTimeField
    datetime_updated = models.DateTimeField
    order_subtotal = models.DecimalField
    status = OrderStatus
