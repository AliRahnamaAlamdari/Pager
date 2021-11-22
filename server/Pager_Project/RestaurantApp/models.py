from django.db import models
from django.contrib.auth.models import AbstractUser


class AppUser(AbstractUser):
    CUSTOMER = 1
    RESTAURANT_ADMIN = 2
    
    ROLE_CHOICES = (
        (CUSTOMER, 'Customer'),
        (RESTAURANT_ADMIN, 'Restaurant_Admin'),
    )


    username = models.CharField(max_length=10 , unique= True)
    email = models.EmailField(unique= True)
    province = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=11)
    adress = models.CharField(max_length=1000)
    # signing_date = models.DateTimeField(null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    def __str__(self):
        return f"username:{self.username}-id:{self.pk}"

class Restaurant(models.Model):
    admin = models.ForeignKey(
        AppUser, on_delete=models.CASCADE, related_name='RestaurantAdmins')
    name = models.CharField(max_length=50)
    province = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    addres = models.CharField(max_length=1000)
    image = models.ImageField(blank = True)

    def __str__(self):
        return f"RestName:{self.name}-RestID:{self.pk}"
    



class FoodGroup(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.name}-{self.pk}"
    

class FoodItem(models.Model):
    name = models.CharField(max_length=45)
    price = models.IntegerField()
    stock = models.IntegerField()
    food_ingredients = models.CharField(max_length=1000)
    image = models.ImageField(blank =True)
    food_unit = models.CharField(max_length=15)
    Food_Group = models.ForeignKey(FoodGroup , on_delete = models.CASCADE , related_name= 'foods')
    Restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='foods')
    
    def __str__(self):
        return self.name
    



