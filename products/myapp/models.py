from django.db import models

class Orders(models.Model):
    order_number = models.CharField('Номер', max_length=10)
    order_data = models.DateField('Дата заказа')
    prod = models.CharField('Products', on_delete=models.PROTECT,null=False)
    cust = models.CharField('Customers', on_delete=models.PROTECT,null=False)
    quantite = models.CharField('Customers', on_delete=models.PROTECT,null=False)
 def __str__(self):
     return self.order_number

 class Meta :


