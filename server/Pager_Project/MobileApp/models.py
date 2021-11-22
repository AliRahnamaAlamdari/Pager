from django.db import models

from RestaurantApp.models import *


class Orders(models.Model):
    User = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name='orders' , blank=True , null=True)
    Restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='orders')
    is_prepaerd = models.BooleanField(default=False)
    dateTime = models.DateTimeField()
    discount = models.IntegerField()
    total_order_price = models.IntegerField()
    transport_cost = models.IntegerField()
    packaging_cost = models.IntegerField() 
    def __str__(self):
        return f"{self.User}-{self.Restaurant}-orderID:{self.pk}"
    

class OrderItem(models.Model):

    Order = models.ForeignKey(
        Orders, on_delete=models.CASCADE, related_name='order_details')
    Food = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    total_food_price = models.IntegerField()
    discount = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"orderID:{self.Order}-FoodID:{self.Food}"
