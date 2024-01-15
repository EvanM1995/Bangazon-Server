from django.db import models


class OrderMenuItems(models.Model):
    menu_items_id = models.IntegerField
    order_id = models.IntegerField
