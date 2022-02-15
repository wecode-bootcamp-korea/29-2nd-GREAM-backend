from django.db import models

class Order(models.Model):
    order_no   = models.UUIDField()
    status_id  = models.ForeignKey('Status', models.DO_NOTHING, related_name = 'order')
    buyer_id   = models.ForeignKey('users.User', models.DO_NOTHING, related_name = 'buyer_id')
    seller_id  = models.ForeignKey('users.User', models.DO_NOTHING, related_name = 'seller_id')
    created_at = models.DateTimeField(auto_now_add = True)    

    class Meta:
        db_table = 'orders'

class Status(models.Model):
    name = models.CharField(max_length = 50, null = False)

    class Meta:
        db_table = 'statuses'
