from django.db import models
from MyApps.models import FoodCategory


# Foods
class Food(models.Model):
    f_category = models.ForeignKey(FoodCategory, on_delete=models.DO_NOTHING)
    f_name = models.CharField(max_length=50)
    f_price = models.FloatField()
    f_description = models.TextField()
    f_secondary_description = models.TextField(default=True)
    f_is_available = models.BooleanField(default=True)
    f_photo = models.ImageField(upload_to="food_images/")

    def __str__(self):
        return self.f_name
