from django.db import models
from matplotlib import category


# Food Category
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# Food Items
class FoodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    secondary_description = models.TextField(default=True)
    availability = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="food_images/")

    def __str__(self):
        return self.name
